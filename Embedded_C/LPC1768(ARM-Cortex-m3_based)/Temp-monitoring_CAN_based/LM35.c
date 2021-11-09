/*(C) Umang Gajera - www.ocfreaks.com
LPC1768/LPC1769 ADC Interfacing Example 1 Source Code using KEIL ARM
More Embedded tutorials @ www.ocfreaks.com/cat/embedded/
License : GPL.*/

#include <lpc17xx.h>
#include <stdio.h>
#include "ocf_lpc176x_lib.h" //contains uart, timer & fputc to retarget printf  

#define VREF       3.3 //Reference Voltage at VREFP pin, given VREFN = 0V(GND)
#define ADC_CLK_EN (1<<12)
#define SEL_AD0_0  (1<<0) //Select Channel AD0.0 
#define CLKDIV     1 //ADC clock-divider (ADC_CLOCK=PCLK/CLKDIV+1) = 12.5Mhz @ 25Mhz PCLK
#define PWRUP      (1<<21) //setting it to 0 will power it down
#define START_CNV  (1<<24) //001 for starting the conversion immediately
#define ADC_DONE   (1U<<31) //define it as unsigned value or compiler will throw #61-D warning
#define ADCR_SETUP_SCM ((CLKDIV<<8) | PWRUP)

volatile uint32_t res;
int result = 0;
float volts = 0;

int mq2(void)
{
	//SystemInit(); //Gets called by Startup code, sets CCLK=100Mhz, PCLK=25Mhz
	//initUART0(); //Initialize UART0 for uart_printf() - both defined in tmr_uart_printf.cpp
	initTimer0(); //For delayMS() - both defined in tmr_uart_printf.cpp

	LPC_SC->PCONP |= ADC_CLK_EN; //Enable ADC clock
	LPC_ADC->ADCR =  ADCR_SETUP_SCM | SEL_AD0_0;
	LPC_PINCON->PINSEL1 |= (1<<14) ; //select AD0.0 for P0.23
	//int result = 0;
	//int res = 0; // change
       // float volts = 0;
	
	//printf("OCFreaks.com LPC176x ADC Tutorial Example 1.\nSoftware Controlled ADC Mode on AD0.0 Channel.\n");
	
	
		LPC_ADC->ADCR |= START_CNV; //Start new Conversion
    res = *(LPC_ADC->ADDR0);
		while((res & ADC_DONE) == 0); //Wait untill conversion is finished
		
		result = (res>>4) & 0xFFF; //12 bit Mask to extract result
		
		volts = (result*VREF)/4096.0; //Convert result to Voltage
		
		//printf("AD0.0 = %dmV\n" , (int)(volts*1000)); //Display milli-volts
		delayMS(500); //Slowing down Updates to 2 Updates per second

	
	return (int)(volts*1000);                 //This won't execute
}
