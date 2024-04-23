#include <wiringPi.h>
#include <stdio.h>
// sudo gcc -o test test.cpp -l wiringPi
int LED_1 = 10;
int LED_2 = 13;

int main() {
    wiringPiSetup();

    pinMode(LED_1,OUTPUT);
    pinMode(LED_2,OUTPUT);

    while(1) {
        digitalWrite(LED_1,HIGH);
        digitalWrite(LED_2,HIGH);
        delay(1000);
        digitalWrite(LED_1,HIGH);
        digitalWrite(LED_2,LOW);
        delay(1000);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,HIGH);
        delay(1000);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,LOW);
        delay(1000);
    }
// GitHub
    return 1;
}