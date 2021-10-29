//Pankaj Chaudhari
// 107
#include "LPC1768.h"
void HextoASCII(unsigned int myValue);

int main ()
{
unsigned int rx;
PINSEL3=0xc0000000; // AD0.5, 
PINSEL0=0x00000050;  //UART initialisation
ADCR=0x01200220;	 // channnel 5 ,6.0 MHz, raise SoC
while((ADGDR&0x80000000)!=0x80000000);	// EoC DONE
rx= (ADGDR&0x0000fff0);
rx=rx>>4;	
 HextoASCII (rx);
}
void HextoASCII(unsigned int myValue)
{

unsigned int d1,d2,d3,d4,i;

//Taking digits one by one
d1=myValue % 0x0A; //Least Significant Digit (LSD).... myValue divided by 10, Remainder = d1
d1 = d1 | 0x30; //make it ASCII

d2=(myValue / 0x0A) % 0x0A;
d2 = d2 | 0x30; //make it ASCII


d3=((myValue/ 0x0A) / 0x0A) % 0x0A;
d3 = d3 | 0x30; //make it ASCII


d4=(((myValue/ 0x0A) / 0x0A) / 0x0A ) % 0x0A ;//Most Sigificant Digit (MSD)
d4 = d4 | 0x30; //make it ASCII
	
U0FCR = 0X07;       // RESET FIFO AND ENABLE IT
U0LCR = 0x80; 
U0DLL = 0x75;
U0DLM = 0x00;
U0LCR = 0x03;
U0TER = 0x80;

	while(1)
	{
	U0THR = d4;
	while(!(U0LSR & 0x20));
	for(i=0;i<255;i++);
	U0THR = d3;
	while(!(U0LSR & 0x20));
	for(i=0;i<255;i++);
	U0THR = d2;
	while(!(U0LSR & 0x20));
	for(i=0;i<255;i++);
	U0THR = d1;
	while(!(U0LSR & 0x20));
	for(i=0;i<255;i++);
	U0THR = '/';
	while(!(U0LSR & 0x20)); // for transferring a character
	for(i=0;i<255;i++);
	}
}
