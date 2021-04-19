/* 
 * File:   LCD_timer.c
 * Author: Pankaj
 *
 * Created on 20 March, 2021, 11:15 AM
 */


#include <xc.h>
#include "configbits.h"
 
void timer_delay()
{
    T0CON=0x08;
    TMR0H=0xE2;
    TMR0L=0xB4;
    T0CONbits.TMR0ON=1;
    while(INTCONbits.TMR0IF==0);
    T0CONbits.TMR0ON=0;
    INTCONbits.TMR0IF=0;
}
void main()
{ TRISBbits.TRISB0=0;
  
  while(1)
  { 
      PORTBbits.RB0=1;
      timer_delay();
      PORTBbits.RB0=0;
      
  }
      
    
}

