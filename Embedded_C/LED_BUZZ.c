/*
 * File:   LED_BUZZ.c
 * Author: PANKAJ CHAUDHARI
 *
 * Created on 6 February, 2021, 12:44 PM
 */

#include <xc.h>
#include "configbits.h"

void delay(int); 

void main(void) 
{   int ms=100;
    TRISDbits.TRISD7=1;
     /////// Led 
     TRISB=0;
    
     if(PORTDbits.RD7==1)
         PORTB=0x0f;
     else
         PORTB=0;
    
     
     /* while(1)
     { int p=0b00001000;
     for(int i=1;i<=3;i++)
     {   PORTB=p;
         delay(ms);
         p=p>>1;
     }
     
     for(int i=1;i<=3;i++)
     {
         PORTB=p;
         p=p<<1;
         delay(ms);    
     } 
     }
      
     */
     
     
     /* PORTBbits.RB0=1;
     delay(ms);
     PORTBbits.RB1=1;
     delay(ms);
     PORTBbits.RB2=1;
     delay(ms);
     PORTBbits.RB3=1;
     delay(ms);
     
     PORTB=0x00;
     
     delay(ms);
     PORTBbits.RB3=1;
     delay(ms);
     PORTBbits.RB2=1;
     delay(ms);
     PORTBbits.RB1=1;
     delay(ms);
     PORTBbits.RB0=1;
     delay(ms);
        */
   
}

void delay(int ms)
{ 
    for(int i=0;i<=ms;i++)
        for(int j=0;j<=1000;j++);
}