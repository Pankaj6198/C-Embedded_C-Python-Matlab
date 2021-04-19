/*
 * File:   Seven_seg.c
 * Author: Pankaj
 *
 * Created on 20 February, 2021, 12:45 PM
 */


#include <xc.h>
#include"configbits.h"
void delay(int); 


void main(void) 
{ int ms=100;
    unsigned char arr[]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f};  
    TRISD=0;
    
    for(int i=0;i<10;i++)
    {
        PORTD=arr[i];
        delay(ms);
    }
}

void delay(int ms)
{ 
    for(int i=0;i<=ms;i++)
        for(int j=0;j<=1000;j++);
}