#include <wiringPi.h>
#include <stdio.h>
// sudo gcc -o test test.cpp -l wiringPi
int LED = 10;

int main() {
    wiringPiSetup();

    pinMode(LED,OUTPUT);

    while(1) {
        digitalWrite(LED,HIGH);
        delay(1000);
        digitalWrite(LED,LOW);
        delay(1000);
    }

    return 1;
}