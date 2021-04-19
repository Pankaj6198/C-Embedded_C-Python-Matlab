/* 
 * File:   ADC_pic18f458.c
 * Author: Pankaj
 *
 * Created on 17 April, 2021, 1:23 PM
 */

#include <xc.h>
#include "configbits_PIC18F458.h"

void delay(int ms)
{ 
    for(int i=0;i<=ms;i++)
        for(int j=0;j<=1000;j++);
        
}
void main()
{
    TRISC=0;
    TRISD=0;
    TRISAbits.TRISA0=1;  // Analog I/P
    ADCON0= 0x81;  // Fosc/64 , channel 0, A/D ON
    ADCON1= 0xCE;  // Right justified , Fosc/64 , (out of 16 bits 10 bits enable from right(lsb))
    
    while(1)
    {
        delay(1); // give A/D channel time to sample
        ADCON0bits.GO=1;  // start converting analog to digital
        while(ADCON0bits.DONE==1);
        PORTC=ADRESL;  // DISPLAY LOW byte on PORTC
        PORTD=ADRESH;  // DISPLAY HIGH byte on PORTD
        delay(250);   // wait for sometime before trying(to convert analog to digital) 
                      // again(the other sample))
    }
    
}

