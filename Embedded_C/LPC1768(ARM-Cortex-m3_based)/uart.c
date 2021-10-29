// PANKAJ CHAUDHARI
// 107
#include "LPC1768.h"
int main()
{
	char data[] = "Pankaj Chaudhari "; // Data to be transmited
	PINSEL0 = 0x00000050;	// Select TXD0 and RXD0 function
  U0FCR = 0x00000007;  // RESET FIFO AND ENABLE IT
	U0LCR = 0x00000080;  // Enable divisor latch
	// pclk = 18MHz, CountVal = 18000000/(16*baudrate)
	U0DLL = 0x00000075; // baud rate = 9600
	U0DLM = 0x00000000;
	U0LCR = 0x00000003; // 8 bit character length, 1 stop bit, disable parity genration and checking 
	U0TER = 0x80; // transmission enable
	
	for(int i=0;data[i]!='\0';i++)
	{		while(!(U0LSR & 0x20));
			U0THR = data[i];
	}
	return 0;
	
}