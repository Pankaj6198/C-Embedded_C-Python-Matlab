/* 
 * File:   serial_com.c
 * Author: PANKAJ
 *
 * Created on 3 April, 2021, 12:01 PM
 */

#include <stdio.h>
#include "configbits.h"

void transmit_data(char *str)
{  
   for(int i=0;str[i]!='\0';i++)
   {
       TXREG=str[i];
       while(PIR1bits.TXIF==0);
   }    
    
}
void delay(int ms)
{ 
    for(int i=0;i<=ms;i++)
        for(int j=0;j<=1000;j++);
}
void main()
{   TRISDbits.TRISD0=1;
    TXSTA=0x20;
    SPBRG=64;//Baud rate=2400,Fosc=10MHz , SPBRG=(((Fosc/(64(2400)))-1)) (156250/2400) - 1 = 65.1 -1= 64.1= 64
    TXSTAbits.TXEN=1;
    RCSTAbits.SPEN=1;
    if(PORTDbits.RD0==0)
    {transmit_data("BE SAFE ");
    while(PORTDbits.RD0==0);
    //delay(100);
    }
    else
    {    transmit_data("GO CORONA "); 
         while(PORTDbits.RD0==1);     
    //delay(100);
    }
    //while(1);
    
    
}

