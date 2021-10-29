#include "LPC1768.h"
int main()
{
unsigned int rx;
//VPBDIV = 0;
PCONP=1<<12;
PINSEL1=0x00004000;	//ADC0.0
ADCR = 0x01200201;	//pclk=18m,fosc=6mhz,adc0.0

while((ADGDR & 0x80000000)!=0x80000000);
rx = (ADGDR & 0x0000FFF0);
rx = rx >> 4;   // shifting is needed to extract data value.	
}
