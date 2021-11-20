#include "LPC1768.h"
#define PRESCALE 18000 //18000 PCLK clock cycles to increment TC by 1ms 

void  initTimer0 (void);      // Function Declaration 
void DelayMs (unsigned int Ms) 
{ 
	T0TCR = 0x02;            //Reset TImer 
	T0TCR = 0x01;           //Enable Timer 
	while(T0TC<Ms)       // wait until timer counter reaches the desired delay 
	T0TCR =0x00;            //Disable timer 

}

int main() 
{ 
	PINSEL0=0x00; 

	initTimer0();     //Initalize Timer0 

	FIO0DIR=0x000000FF;    // Set P0.0 to P0.7 as o/p 
	while(1) 
	{ 
		FIO0SET=0x000000FF ;   // Turn on LEDs 
		DelayMs(500);                // 0.5 second Delay 
		FIO0CLR=0x000000FF;   // Turn off LED 
		DelayMs(500);               // 0.5 second Delay 
	} 
	return 0;
} 

void initTimer0(void) 
{ 
	T0CTCR = 0x0; // Timer mode 
	T0PR =PRESCALE-1; //value in Decimal – Increment T0TC at every 60000 clock cycles 			// Count begins from 0 hence subtracting 1.	60000 clock cycles                     		//@60MHz = 1 ms 
	T0TCR = 0x02; //Reset Timer 
} 
