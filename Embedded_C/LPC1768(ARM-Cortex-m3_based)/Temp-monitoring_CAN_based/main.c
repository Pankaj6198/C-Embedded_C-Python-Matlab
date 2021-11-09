/*----------------------------------------------------------------------------
 * Name:    CanDemo.c
 * Purpose: CAN example for LPC17xx with LPC176x
 * Version: V1.00
 * Note(s):
 *----------------------------------------------------------------------------
 * This file is part of the uVision/ARM development tools.
 * This software may only be used under the terms of a valid, current,
 * end user licence from KEIL for a compatible version of KEIL software
 * development tools. Nothing else gives you the right to use this software.
 *
 * This software is supplied "AS IS" without warranties of any kind.
 *
 * Copyright (c) 2009 Keil - An ARM Company. All rights reserved.
 *----------------------------------------------------------------------------
 * History:
 *          V1.00 Initial Version
 *----------------------------------------------------------------------------*/
//#include "LPC1768.h"
#include "HEADER.h"
#include "ocf_lpc176x_lib.h"
#include <LPC17xx.h>                            /* LPC17xx definitions */
#include <stdio.h>
#include "CAN.h"                                /* LPC1768 CAN adaption layer */
#include "GLCD.h"                               /* GLCD function prototypes */
//#include "LED.h"                                /* LED function prototypes */
#include "ADC.h"  
#include "LM35.h"                              /* ADC function prototypes */


unsigned int val_Tx = 0, val_Rx = 0;            /* Globals used for display */

char hex_chars[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};


/*----------------------------------------------------------------------------
  insert a delay time.
 *----------------------------------------------------------------------------*/
void delay(unsigned int nCount)	{

  for(; nCount != 0; nCount--);
}


/*------------------------------------------------------------------------------
  convert one byte to string in hexadecimal notation
 *------------------------------------------------------------------------------*/
void Hex_Str (unsigned int hex, char *str) {
   unsigned int arr[5],i=0,n=0;
  while(hex!=0)
  {
  arr[i]=hex%10;
  hex=hex/10;
  i++;
  }
  while(i!=0)
  {
  n=arr[i-1];
  
  *str++=hex_chars[n];
  i--;
  }
  *str++=' ';
}

/*------------------------------------------------------------------------------
  Initialises the Analog/Digital converter
 *------------------------------------------------------------------------------*/
void adc_Init (void) {

  ADC_init();                                     /* initialise ADC */
}

/*------------------------------------------------------------------------------
  read a converted value from the Analog/Digital converter
 *------------------------------------------------------------------------------*/
unsigned char adc_Get (void) {
  unsigned char val;

  ADC_startCnv();                                 /* start A/D conversion */
  val = (ADC_getCnv() & 0xFF);                    /* Scale value to 8 bits */
  ADC_stopCnv();                                  /* stop A/D conversion */
	
  return (val);
}

/*----------------------------------------------------------------------------
  display transmit and receieve values
 *---------------------------------------------------------------------------*/
void val_display (void) {
  static char disp_buf[] = "smoke:      Recv:  ";   /* display string */

  Hex_Str(val_Tx, &disp_buf[ 7]);                 /* display Tx and Rx values to LCD disp */
 Hex_Str(val_Rx, &disp_buf[18]);
  GLCD_displayStringLn(Line6, (uint8_t*)disp_buf);/* print string to LCD */
 // LED_out (val_Rx);                               /* display RX val on LEDs */

  delay (1000000);                                /* Wait wait a while */
}


/*----------------------------------------------------------------------------
  initialize CAN interface
 *----------------------------------------------------------------------------*/
void can_Init (void) {

  CAN_setup (1);                                  /* setup CAN Controller #1 */
  CAN_setup (2);                                  /* setup CAN Controller #2 */
  CAN_wrFilter (1, 33, STANDARD_FORMAT);          /* Enable reception of messages */

  CAN_start (1);                                  /* start CAN Controller #2 */
  CAN_start (2);                                  /* start CAN Controller #2 */

  CAN_waitReady (1);                              /* wait til tx mbx is empty */
  CAN_waitReady (2);                              /* wait til tx mbx is empty */
}



/*----------------------------------------------------------------------------
  MAIN function
 *----------------------------------------------------------------------------*/

int main (void)  {
  int i;
  LPC_GPIO2->FIODIR =0X00000003;
  SystemInit();                                   /* initialize MCU clocks */

  adc_Init ();                                    /* initialise A/D converter */
 // LED_init ();                                    /* Initialize the LEDs */
  can_Init ();                                    /* initialise CAN interface */

  GLCD_init();                                    /* Initialize the GLCD */
  GLCD_clear(Black);                              /* Clear the GLCD */

  GLCD_setBackColor(Blue);                        /* Set the Back Color */
  GLCD_setTextColor(White);                       /* Set the Text Color */
  GLCD_displayStringLn(Line0, "INDUSTRIAL PARAMETER  ");
  GLCD_displayStringLn(Line1, "     MONITORING     ");
  GLCD_displayStringLn(Line2, "  USING CAN ");
   GLCD_displayStringLn(Line8, "  Rollno 107 ");
  GLCD_setBackColor(Black);                       /* Set the Back Color */
  GLCD_setTextColor(Yellow);                        /* Set the Text Color */

  GLCD_displayStringLn(Line5, " CAN DEMO ");

  CAN_TxMsg[1].id = 33;                           /* initialise message to send */
  for (i = 0; i < 8; i++) CAN_TxMsg[0].data[i] = 0;
  CAN_TxMsg[1].len = 1;
  CAN_TxMsg[1].format = STANDARD_FORMAT;
  CAN_TxMsg[1].type = DATA_FRAME;

  while (1) 
  {
     LPC_GPIO2->FIOCLR=0x00000001;
    val_Tx = mq2();                         /* TX value changes in any case */
    printf("tx= %d\n",val_Tx);
   if(val_Tx < 1000)
      {
              if (CAN_TxRdy[1])
              {                           /* tx message on CAN Controller #2 */
              CAN_TxRdy[1] = 0;

              CAN_TxMsg[1].data[0] = 1;             /* data[0] field = ADC value */
              printf("1 sent\n");
              CAN_wrMsg (2, &CAN_TxMsg[1]);               /* transmit message */
              }
      }
       else
      {
              if (CAN_TxRdy[1])
              {                           /* tx message on CAN Controller #2 */
              CAN_TxRdy[1] = 0;
              
              CAN_TxMsg[1].data[0] = 2;             /* data[0] field = ADC value */
              printf("2 sent\n");
              CAN_wrMsg (2, &CAN_TxMsg[1]);               /* transmit message  via CAN*/
              }
      }
    delay (10000000);                                /* Wait a while to receive the message */

 if (CAN_RxRdy[0]) {                           /* rc message on CAN Controller #1 */
    CAN_RxRdy[0] = 0;

      
	 val_Rx = CAN_RxMsg[0].data[0];
          printf("Rx= %d\n",val_Rx);
          if(val_Rx == 2 )
          {
            printf("2 rec\n");
            LPC_GPIO2->FIOSET =0x00000001;
            delay(10000000  );


          }
          else
          {
                printf("1 rec\n");
                LPC_GPIO2->FIOCLR=0x00000001;
          }
      
    } 
    val_display ();                               /* display TX and RX values */

  }
 }