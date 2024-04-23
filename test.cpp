#include <wiringPi.h>
#include <stdio.h>
// sudo gcc -o test test.cpp -l wiringPi
int LED_1 = 10;
int LED_2 = 13;
int LED_3 = 16;

int WAIT_TIME_MS = 500;

int main() {
    wiringPiSetup();

    pinMode(LED_1,OUTPUT);
    pinMode(LED_2,OUTPUT);
    pinMode(LED_3,OUTPUT);

    while(1) {
        digitalWrite(LED_1,HIGH);
        digitalWrite(LED_2,HIGH);
        digitalWrite(LED_3,HIGH);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,HIGH);
        digitalWrite(LED_2,LOW);
        digitalWrite(LED_3,LOW);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,HIGH);
        digitalWrite(LED_3,LOW);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,LOW);
        digitalWrite(LED_3,HIGH);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,LOW);
        digitalWrite(LED_3,LOW);
        delay(WAIT_TIME_MS);
    }

    return 1;
}