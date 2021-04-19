/*
 * File:   Seven_seg_switch.c
 * Author: Pankaj
 *
 * Created on 20 February, 2021, 12:45 PM
 */


#include <xc.h>
#include"configbits.h"
void delay(int); 

void main(void) 
{  int ms=100;
  unsigned char arr[]={0x3f,0x06,0x5b,0x4f};  
    TRISD=0;
    TRISC=1;    
    if(PORTCbits.RC0==1)
        PORTD=arr[0];
    if(PORTCbits.RC1==1)
        PORTD=arr[1];
    if(PORTCbits.RC2==1)
        PORTD=arr[2];
    if(PORTCbits.RC3==1)
        PORTD=arr[3];
 }

void delay(int ms)
{ 
    for(int i=0;i<=ms;i++)
        for(int j=0;j<=1000;j++);
}