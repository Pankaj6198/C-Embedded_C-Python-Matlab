/*
 * File:   LCD_16x2.c
 * Author: PANKAJ CHAUDHARI
 *
 * Created on 27 February, 2021, 12:20 PM
 */

#include <xc.h>
#include "configbits.h"

#define rs PORTCbits.RC0
#define rw PORTCbits.RC1
#define en PORTCbits.RC2

void delay(int ms)
{ 
    for(int i=0;i<=ms;i++)
        for(int j=0;j<=1000;j++);
}

void LCD_DATA(unsigned char data)
{
    PORTD= data;
    rs=1;
    rw=0;
    en=1;
    delay(10);
    en=0;
}

void LCD_CMD(unsigned char cmd)
{
    PORTD= cmd;
    rs=0;
    rw=0;
    en=1;
    delay(10);
    en=0;
}

void disp_string(unsigned char *str)
{
    for(int i=0;str[i]!='\0';i++)
        LCD_DATA(str[i]);

}

void init_lcd()
{ LCD_CMD(0x38);
  LCD_CMD(0x06);
  LCD_CMD(0x0C);
  LCD_CMD(0x01);  
}

void main() 
{   TRISC=0x00;
    TRISD=0x00;
   
    init_lcd();
    
  while(1)
  {
      LCD_CMD(0x84);
      disp_string("PANKAJ");
      LCD_CMD(0xC4);
      disp_string("CHAUDHARI");
  }
    
    
}