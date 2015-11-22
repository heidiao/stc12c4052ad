#include <STC12C2052AD.H>
void UART_init (void){                                                                                                                          
    TMOD = 0x20;
    SCON = 0x50;
    TH1 = 0xF3;
    TL1 = 0xF3;
    PCON = 0x80;
    TR1 = 1;
}

void main (void){
    unsigned char UART_data;
    UART_init();
    while(1){
        if (RI == 1){
            UART_data = SBUF;
            RI = 0;

            SBUF = UART_data;
            while(TI == 0);
            TI = 0;
        }
    }
}
