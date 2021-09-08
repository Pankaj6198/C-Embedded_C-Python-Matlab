/* File:   PC_108_MCI_OEA2.c
 * Author: Pankaj
 * Created on 7 May, 2021, 6:31 PM
 */
#include <xc.h>
#include "configbits.h"   // User defined header file for bits configuration

void transmit_data(char *str)   // To Transmit data serially
{  for(int i=0;str[i]!='\0';i++)
   {   TXREG=str[i];
       while(PIR1bits.TXIF==0); 
   }    
}

void main()
{   TRISBbits.TRISB6=1;
    TXSTA=0x20;  // TXEN = 1
    RCSTAbits.SPEN=1; // Serial port enable
    if(PORTBbits.RB6==0)     // when S/W is OFF
     {  TXSTAbits.BRGH=0; // Low baud rate
        SPBRG=32;//Baud rate=4800,Fosc=10MHz,BRGH=0,SPBRG=(((Fosc/(64(4800)))-1))=(156250/4800) - 1 = 31.5 = 32
        transmit_data("LOW BR");
     }
    else
     {  TXSTAbits.BRGH=1; // High baud rate
        SPBRG=64;//Baud rate=9600,Fosc=10MHz,BRGH=1 ,SPBRG=(((Fosc/(16(9600)))-1))=(625000/9600)-1 = 64.1= 64 
        transmit_data("HIGH BR");      
     }   
    while(1);
}
