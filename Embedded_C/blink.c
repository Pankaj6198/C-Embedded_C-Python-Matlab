// Connect 8 LED  at Port2.0-7


#include "LPC1768.h"
void delay(void)
{
	for(int i=0;i<100000;i++);
}

int main()
{ 
	PINSEL4 = 0x00000000; // P2 as GPIO
	FIO2DIR = 0x000000FF; // P2.0 to P2.7 as O/P
	while(1)
	{
		FIO2SET = 0x000000FF; // ON
		delay();
		FIO2CLR = 0x000000FF;
		delay();
	}

}