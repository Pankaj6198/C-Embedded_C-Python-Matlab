/*----------------------------------------------------------------------------
 * Name:    Can.c
 * Purpose: CAN interface for for LPC17xx with LPC176x
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

#include <LPC17xx.H>                             /* LPC17xx definitions */
#include "CAN.h"                                 /* LPC17xx CAN adaption layer */
#include "HEADER.h"
#include <stdio.h>
CAN_msg       CAN_TxMsg[2];                      /* CAN message for sending */
CAN_msg       CAN_RxMsg[2];                      /* CAN message for receiving */                                

unsigned int  CAN_TxRdy[2] = {0,0};              /* CAN HW ready to transmit a message */
unsigned int  CAN_RxRdy[2] = {0,0};              /* CAN HW received a message */


#define  PCLK            18000000                /* Peripheral clock, depends on VPBDIV */
//TO REMOVE ERROR
#define SC LPC_SC
#define PINCON LPC_PINCON
#define CANAF LPC_CANAF
/* Values of bit time register for different baudrates
   NT = Nominal bit time = TSEG1 + TSEG2 + 3
   SP = Sample point     = ((TSEG2 +1) / (TSEG1 + TSEG2 + 3)) * 100%
                                            SAM,  SJW, TSEG1, TSEG2, NT,  SP */
const uint32_t CAN_BIT_TIME[] = {          0, /*             not used             */
                                           0, /*             not used             */
                                           0, /*             not used             */
                                           0, /*             not used             */
                                  0x0001C000, /* 0+1,  3+1,   1+1,   0+1,  4, 75% */
                                           0, /*             not used             */
                                  0x0012C000, /* 0+1,  3+1,   2+1,   1+1,  6, 67% */
                                           0, /*             not used             */
                                  0x0023C000, /* 0+1,  3+1,   3+1,   2+1,  8, 63% */
                                           0, /*             not used             */
                                  0x0025C000, /* 0+1,  3+1,   5+1,   2+1, 10, 70% */
                                           0, /*             not used             */
                                  0x0036C000, /* 0+1,  3+1,   6+1,   3+1, 12, 67% */
                                           0, /*             not used             */
                                           0, /*             not used             */
                                  0x0048C000, /* 0+1,  3+1,   8+1,   4+1, 15, 67% */
                                  0x0049C000, /* 0+1,  3+1,   9+1,   4+1, 16, 69% */
                                };

/*----------------------------------------------------------------------------
  configure the requested baudrate.  CAN controller (1..2)
 *----------------------------------------------------------------------------*/
static void CAN_cfgBaudrate (uint32_t ctrl, uint32_t baudrate)  {
  CAN_TypeDef *pCAN = (ctrl == 1) ? CAN1 : CAN2; /* select CAN controller */
  uint32_t result = 0;
  uint32_t nominal_time;

  /* Determine which nominal time to use for PCLK and baudrate */
  if (baudrate <= 500000)  {
    nominal_time = 12;
  }  else if (((PCLK / 1000000) % 15) == 0)  {
    nominal_time = 15;
  }  else if (((PCLK / 1000000) % 16) == 0)  {
    nominal_time = 16;
  }  else  {
    nominal_time = 10;
  }

  /* Prepare value appropriate for bit time register */
  result  = (PCLK / nominal_time) / baudrate - 1;
  result &= 0x000003FF;
  result |= CAN_BIT_TIME[nominal_time];

  pCAN->BTR  = result;                           /* Set bit timing */
  printf("baud %d\n",baudrate);
}


/*----------------------------------------------------------------------------
  setup CAN interface.  CAN controller (1..2)
 *----------------------------------------------------------------------------*/
void CAN_setup (int ctrl)  {
  CAN_TypeDef *pCAN = (ctrl == 1) ? CAN1 : CAN2; /* select CAN controller */

  if (ctrl == 1) {
    SC->PCONP       |=  (1 << 13);               /* Enable power to CAN1 block */
    PINCON->PINSEL0 |=  (1 <<  0);               /* Pin P0.0 used as RD1 (CAN1) */
    PINCON->PINSEL0 |=  (1 <<  2);               /* Pin P0.1 used as TD1 (CAN1) */
    
    NVIC_EnableIRQ(CAN_IRQn);                    /* Enable CAN interrupt */
  } else {
    SC->PCONP       |=  (1 << 14);               /* Enable power to CAN2 block */
    PINCON->PINSEL4 |=  (1 << 14);               /* Pin P2.7 used as RD2 (CAN2) */
    PINCON->PINSEL4 |=  (1 << 16);               /* Pin P2.8 used as TD2 (CAN2) */
    
    NVIC_EnableIRQ(CAN_IRQn);                    /* Enable CAN interrupt */
  }

  CANAF->AFMR = 2;                               /* By default filter is not used */
  pCAN->MOD   = 1;                               /* Enter reset mode */
  pCAN->IER   = 0;                               /* Disable all interrupts */
  pCAN->GSR   = 0;                               /* Clear status register */
  CAN_cfgBaudrate(ctrl, 500000);                 /* Set bit timing */
  pCAN->IER   = 0x0003;                          /* Enable Tx and Rx interrupt */
}


/*----------------------------------------------------------------------------
  leave initialisation mode.  CAN controller (1..2)
 *----------------------------------------------------------------------------*/
void CAN_start (int ctrl)  {
  CAN_TypeDef *pCAN = (ctrl == 1) ? CAN1 : CAN2; /* select CAN controller */

  pCAN->MOD = 0;                                 /* Enter normal operating mode */
}

/*----------------------------------------------------------------------------
  check if transmit mailbox is empty
 *----------------------------------------------------------------------------*/
void CAN_waitReady (int ctrl)  {
  CAN_TypeDef *pCAN = (ctrl == 1) ? CAN1 : CAN2; /* select CAN controller */

  while ((pCAN->SR & (1<<2)) == 0);              /* Transmitter ready for transmission */
  CAN_TxRdy[ctrl-1] = 1;
}

/*----------------------------------------------------------------------------
  wite a message to CAN peripheral and transmit it.  CAN controller (1..2)
 *----------------------------------------------------------------------------*/
void CAN_wrMsg (int ctrl, CAN_msg *msg)  {
  CAN_TypeDef *pCAN = (ctrl == 1) ? CAN1 : CAN2; /* select CAN controller */
  uint32_t CANData;

  CANData = (((int) msg->len) << 16)     & 0x000F0000 | 
            (msg->format == EXTENDED_FORMAT ) * 0x80000000 |
            (msg->type   == REMOTE_FRAME)     * 0x40000000;

  if (pCAN->SR & (1<<2))  {                      /* Transmit buffer 1 free */
    pCAN->TFI1  = CANData;                       /* Write frame informations */
    pCAN->TID1 = msg->id;                        /* Write CAN message identifier */
    pCAN->TDA1 = *(uint32_t *) &msg->data[0];    /* Write first 4 data bytes */
    pCAN->TDB1 = *(uint32_t *) &msg->data[4];    /* Write second 4 data bytes */
    //pCAN->CMR  = 0x31;                           /* Select Tx1 for Self Tx/Rx */
    pCAN->CMR  = 0x21;                           /* Start transmission without loop-back */
  }
}

/*----------------------------------------------------------------------------
  read a message from CAN peripheral and release it.  CAN controller (1..2)
 *----------------------------------------------------------------------------*/
void CAN_rdMsg (int ctrl, CAN_msg *msg)  {
  CAN_TypeDef *pCAN = (ctrl == 1) ? CAN1 : CAN2; /* select CAN controller */
  uint32_t CANData;

                                                 /* Read frame informations */
  CANData = pCAN->RFS;
  msg->format   = (CANData & 0x80000000) == 0x80000000;
  msg->type     = (CANData & 0x40000000) == 0x40000000;
  msg->len      = ((uint8_t)(CANData >> 16)) & 0x0F;

  msg->id = pCAN->RID;                           /* Read CAN message identifier */

  if (msg->type == DATA_FRAME)  {                /* Read the data if received message was DATA FRAME  */ 
    *(uint32_t *) &msg->data[0] = pCAN->RDA;
    *(uint32_t *) &msg->data[4] = pCAN->RDB;
  }
}


/*----------------------------------------------------------------------------
  setup acceptance filter.  CAN controller (1..2)
 *----------------------------------------------------------------------------*/
void CAN_wrFilter (int ctrl, int id, int format)  {
  static int CAN_std_cnt = 0;
  static int CAN_ext_cnt = 0;
         uint32_t buf0, buf1;
         int cnt1, cnt2, bound1;

  /* Acceptance Filter Memory full */
  if ((((CAN_std_cnt + 1) >> 1) + CAN_ext_cnt) >= 512)
    return;                                       /* error: objects full */

  /* Setup Acceptance Filter Configuration 
    Acceptance Filter Mode Register = Off  */                                 
  LPC_CANAF->AFMR = 0x00000001;

  if (format == STANDARD_FORMAT)  {              /* Add mask for standard identifiers */
    id |= (ctrl-1) << 13;                        /* Add controller number */
    id &= 0x0000F7FF;                            /* Mask out 16-bits of ID */

    /* Move all remaining extended mask entries one place up                 
       if new entry will increase standard ID filters list   */
    if ((CAN_std_cnt & 0x0001) == 0 && CAN_ext_cnt != 0) {
      cnt1   = (CAN_std_cnt >> 1);
      bound1 = CAN_ext_cnt;
      buf0   = LPC_CANAF_RAM->mask[cnt1];
      while (bound1--)  {
        cnt1++;
        buf1 = LPC_CANAF_RAM->mask[cnt1];
        LPC_CANAF_RAM->mask[cnt1] = buf0;
        buf0 = buf1;
      }        
    }

    if (CAN_std_cnt == 0)  {                     /* For entering first  ID */
      LPC_CANAF_RAM->mask[0] = 0x0000FFFF | (id << 16);
    }  else if (CAN_std_cnt == 1)  {             /* For entering second ID */
      if ((LPC_CANAF_RAM->mask[0] >> 16) > id)
        LPC_CANAF_RAM->mask[0] = (LPC_CANAF_RAM->mask[0] >> 16) | (id << 16);
      else
        LPC_CANAF_RAM->mask[0] = (LPC_CANAF_RAM->mask[0] & 0xFFFF0000) | id;
    }  else  {
      /* Find where to insert new ID */
      cnt1 = 0;
      cnt2 = CAN_std_cnt;
      bound1 = (CAN_std_cnt - 1) >> 1;
      while (cnt1 <= bound1)  {                  /* Loop through standard existing IDs */
        if ((LPC_CANAF_RAM->mask[cnt1] >> 16) > id)  {
          cnt2 = cnt1 * 2;
          break;
        }
        if ((LPC_CANAF_RAM->mask[cnt1] & 0x0000FFFF) > id)  {
          cnt2 = cnt1 * 2 + 1;
          break;
        }
        cnt1++;                                  /* cnt1 = U32 where to insert new ID */
      }                                          /* cnt2 = U16 where to insert new ID */

      if (cnt1 > bound1)  {                      /* Adding ID as last entry */
        if ((CAN_std_cnt & 0x0001) == 0)         /* Even number of IDs exists */
          LPC_CANAF_RAM->mask[cnt1]  = 0x0000FFFF | (id << 16);
        else                                     /* Odd  number of IDs exists */
          LPC_CANAF_RAM->mask[cnt1]  = (LPC_CANAF_RAM->mask[cnt1] & 0xFFFF0000) | id;
      }  else  {
        buf0 = LPC_CANAF_RAM->mask[cnt1];            /* Remember current entry */
        if ((cnt2 & 0x0001) == 0)                /* Insert new mask to even address */
          buf1 = (id << 16) | (buf0 >> 16);
        else                                     /* Insert new mask to odd  address */
          buf1 = (buf0 & 0xFFFF0000) | id;
     
        LPC_CANAF_RAM->mask[cnt1] = buf1;            /* Insert mask */

        bound1 = CAN_std_cnt >> 1;
        /* Move all remaining standard mask entries one place up */
        while (cnt1 < bound1)  {
          cnt1++;
          buf1  = LPC_CANAF_RAM->mask[cnt1];
          LPC_CANAF_RAM->mask[cnt1] = (buf1 >> 16) | (buf0 << 16);
          buf0  = buf1;
        }

        if ((CAN_std_cnt & 0x0001) == 0)         /* Even number of IDs exists */
          LPC_CANAF_RAM->mask[cnt1] = (LPC_CANAF_RAM->mask[cnt1] & 0xFFFF0000) | (0x0000FFFF);
      }
    }
    CAN_std_cnt++;
  }  else  {                                     /* Add mask for extended identifiers */
    id |= (ctrl-1) << 29;                        /* Add controller number */

    cnt1 = ((CAN_std_cnt + 1) >> 1);
    cnt2 = 0;
    while (cnt2 < CAN_ext_cnt)  {                /* Loop through extended existing masks */
      if (LPC_CANAF_RAM->mask[cnt1] > id)
        break;
      cnt1++;                                    /* cnt1 = U32 where to insert new mask */
      cnt2++;
    }

    buf0 = LPC_CANAF_RAM->mask[cnt1];                /* Remember current entry */
    LPC_CANAF_RAM->mask[cnt1] = id;                  /* Insert mask */

    CAN_ext_cnt++;

    bound1 = CAN_ext_cnt - 1;
    /* Move all remaining extended mask entries one place up */
    while (cnt2 < bound1)  {
      cnt1++;
      cnt2++;
      buf1 = LPC_CANAF_RAM->mask[cnt1];
      LPC_CANAF_RAM->mask[cnt1] = buf0;
      buf0 = buf1;
    }        
  }
  
  /* Calculate std ID start address (buf0) and ext ID start address (buf1) */
  buf0 = ((CAN_std_cnt + 1) >> 1) << 2;
  buf1 = buf0 + (CAN_ext_cnt << 2);

  /* Setup acceptance filter pointers */
  CANAF->SFF_sa     = 0;
  CANAF->SFF_GRP_sa = buf0;
  CANAF->EFF_sa     = buf0;
  CANAF->EFF_GRP_sa = buf1;
  CANAF->ENDofTable = buf1;

  CANAF->AFMR = 0x00000000;                      /* Use acceptance filter */
}


/*----------------------------------------------------------------------------
  CAN interrupt handler
 *----------------------------------------------------------------------------*/
void CAN_IRQHandler (void)  {
  volatile uint32_t temp;

  if (CAN1->GSR & (1 << 0)) {                    /* CAN Controller #1 meassage is received */
	CAN_rdMsg (1, &CAN_RxMsg[0]);                /*  read the message */
    CAN1->CMR = (1 << 2);                        /* Release receive buffer */

    CAN_RxRdy[0] = 1;                            /*  set receive flag */
  }

  if (CAN2->GSR & (1 << 0)) {                    /* CAN Controller #2 meassage is received */
	CAN_rdMsg (2, &CAN_RxMsg[1]);                /*  read the message */
    CAN2->CMR = (1 << 2);                        /* Release receive buffer */

    CAN_RxRdy[1] = 1;                            /*  set receive flag */
  }

  if (CAN1->GSR & (1 << 3)) {                    /* CAN Controller #1 meassage is transmitted */
	CAN_TxRdy[0] = 1; 
  }

  if (CAN2->GSR & (1 << 3)) {                    /* CAN Controller #2 meassage is transmitted */
	CAN_TxRdy[1] = 1; 
  }

  temp = CAN1->ICR;                              /* clear interrupts */
  temp = CAN2->ICR;
}
