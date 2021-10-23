// PANKAJ CHAUDHARI
// 107
// GLCD Interfacing : Control Lines [ P1.25(RW) to P1.26(EN) ]
//  (KS108 128x64)    Data Lines [ P0.4(D0) to P0.11(D7)]                

#include "LPC1768.h"
#include "image.h"  // Contains an Integer Array with Hex values of Emoji_Image

#define ldata 0x00000FF0
#define EN 1<<26
#define RS 1<<25
#define CS1 1<<27
#define CS2 1<<28
#define RW 1<<29

void delay(unsigned int ms)
{
	for(int i=0;i<ms;i++)
	for(int j=0;j<5000;j++);
}

void GLCD_CMD(char val)
{
	FIO0CLR = ldata;
	FIO0SET = val<<4 ; // left shift by 4, as Data lines starts from P0.4
  FIO1CLR = RS ; // RS = 0 (Command Register)
	FIO1CLR = RW ; // RW = 0
	FIO1SET = EN;
	delay(10);
	FIO1CLR = EN;
}

void GLCD_Data(unsigned int data)
{
	FIO0CLR = ldata;
	FIO0SET = data<<4; // left shift by 4, as Data lines starts from P0.4
	FIO1SET = RS;
	FIO1CLR = RW; // DATA WRITE OPERATION
  FIO1SET = EN;
	delay(10);
	FIO1CLR = EN;
}

void GLCD_Disp(unsigned int *Emoji_img)
{
	for(int i=0;i<8;i++)
	{ 
		//LEFT HALF
	  FIO1SET = CS1; // SELECT CONTROLLER 1
		FIO1CLR = CS2; 
		GLCD_CMD(0XB8|i); // Increment page address
		GLCD_CMD(0x40);   // SET ADDRESS
		for(int j=0;j<64;j++)
		  GLCD_Data(Emoji_img[(i*128)+j]);
/*******************************************/
     // RIGHT HALF	
    FIO1CLR = CS1;  // SELECT CONTROLLER 2
		FIO1SET = CS2;
		GLCD_CMD(0XB8|i);  // Increment page address
		GLCD_CMD(0x40);   // SET ADDRESS
		for(int j=64;j<128;j++)
		  GLCD_Data(Emoji_img[(i*128)+j]);
	}
}

int main()
{ 
	PINSEL3 = 0x00000000; // P1 as GPIO
	PINSEL0 = 0x00000000; // P0 a GPIO
	FIO1DIR = 0x3E000000; // Configuring pins as O/P
	FIO0DIR = 0x00000FF0; // Configuring pins as O/P
  FIO1SET = CS1;
	FIO2SET = CS2;
	
	GLCD_CMD(0x3F); // Display ON
  delay(10);
	GLCD_CMD(0x40); // Set Y address as 0 (Range:0-64)
  delay(2000);
  GLCD_CMD(0xB8); // Set X address as 0 (Page Address)[Range:0-7]
  delay(2000);
	GLCD_CMD(0xC0); // Set Z address as 0 (Range:64-128)
  delay(2000);
	GLCD_Disp(Emoji_img);
	delay(2000);
	
}
