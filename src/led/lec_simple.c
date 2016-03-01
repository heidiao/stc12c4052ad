#include <STC12C2052AD.H>                                                                                                                       
sbit LED7 = P1^7;

void main (void){
    void delay(unsigned int);
	while(1){
		LED7=1;
		delay(10000000);
		LED7=0;
		delay(10000000);
    }
}

void delay (unsigned int count){
    unsigned int i;
	for(i=1;i<=count;i++);
}
