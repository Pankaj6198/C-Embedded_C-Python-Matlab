/* 
 * File:   PS1.c
 * Author: Pankaj
 *
 * Created on 10 April, 2021, 12:13 PM
 */

/* PS:
Display your name and roll no in lcd and display even numbers in descending order in seven segment
Else display no data in lcd and ascending order even number in seven segment
*/
#include <xc.h>
#include "configbits.h"

#define rs PORTCbits.RC0
#define rw PORTCbits.RC1
#define en PORTCbits.RC2

void timer_delay()
{
    T0CON=0x07;
    TMR0H=0xBE;
    TMR0L=0xBC;
    T0CONbits.TMR0ON=1;
    while(INTCONbits.TMR0IF==0);
    T0CONbits.TMR0ON=0;
    INTCONbits.TMR0IF=0;
}

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
{   int ms=100;
    unsigned char arr[]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f};  
    TRISB=0x00;
    TRISCbits.TRISC0=0x00;
    TRISCbits.TRISC1=0x00;
    TRISCbits.TRISC2=0x00;
    TRISCbits.TRISC3=0x01;
    TRISD=0x00;
    TRISBbits.TRISB0=0;
    init_lcd();
    while(1)
    { while(PORTCbits.RC3==0)
      {// LCD INTERFACING
        LCD_CMD(0x80);
        disp_string("PANKAJ CHAUDHARI");
        LCD_CMD(0xC2);
        disp_string("108");
        timer_delay();
        LCD_CMD(0x1);
     // 7 segment interfacing 
        
        for(int i=0;i<10;i+=2)
        {
            PORTB=arr[i];
            delay(ms);
        }
        break;
       }  
    while(PORTCbits.RC3=1)
    {   LCD_CMD(0x83);
        disp_string("NO DATA");
        timer_delay();
        LCD_CMD(0x1);
        for(int i=8;i>=0;i-=2)
        {
            PORTB=arr[i];
            delay(ms);
        }
        break;
    }
    
    }
   
}
