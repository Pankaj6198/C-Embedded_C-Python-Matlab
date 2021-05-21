/* 
 * File:   PWM_motor.c
 * Author: Pankaj
 *
 * Created on 27 April, 2021, 10:13 AM
 */

#include <xc.h>
#include "configbits.h"

void main() 
{
    TRISCbits.TRISC2=0;
    CCP1CON=0x3C;
    PR2=100;        
    T2CON=0x01;    //4 prescaler
    CCPR1L=25  ;    // 25% duty cycle
    while(1)
    {
       TMR2=0;
       PIR1bits.TMR2IF=0;
       T2CONbits.TMR2ON=1;
       while(PIR1bits.TMR2IF==0);
    }

}

