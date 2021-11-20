#include "LPC1768.h"

void delay (unsigned int time)
{
unsigned int i,j;
for (i=0;i<time;i++)
 for(j=0;j<20000;j++);
}
 

int main ()
{

unsigned int period = 10000, i;

PINSEL3= 0x00020000; // configure pin P1.24 as PWWM1.5
PCONP =1<<6 ; // enable the PWM peripheral
PWM1CTCR = 0x00000000 ; // select the timer mode
PWM1PR = 0x00 ; //Prescale register -TC will increment at every PR+1
PWM1MCR= 0x00000002 ; //reset on MR0
PWM1MR0= 10000 ; // highest count held by MR0 , set the period
PWM1PCR = 0x00002000; //enable PWM1.5 in single edge mode
PWM1TCR = 0x00000009; //enable PWM and TC

while(1)
{
 for (i=10;i>0;i--)
 {
 PWM1MR5 = i*period/10; //change the duty cycle
PWM1LER= 0x00000020 ; // PWM1.5 lathc enable
delay (1000); // delay
 }
}

}