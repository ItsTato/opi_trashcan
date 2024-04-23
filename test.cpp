#include <wiringPi.h>
#include <stdio.h>
// sudo gcc -o test test.cpp -l wiringPi
int LED_1 = 10;
int LED_2 = 13;
int LED_3 = 16;
int LED_4 = 3;

int WAIT_TIME_MS = 350;

int main() {
    wiringPiSetup();

    pinMode(LED_1,OUTPUT);
    pinMode(LED_2,OUTPUT);
    pinMode(LED_3,OUTPUT);
    pinMode(LED_4,OUTPUT);

    while(1) {
        digitalWrite(LED_1,HIGH);
        digitalWrite(LED_2,HIGH);
        digitalWrite(LED_3,HIGH);
        digitalWrite(LED_4,HIGH);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,HIGH);
        digitalWrite(LED_2,LOW);
        digitalWrite(LED_3,LOW);
        digitalWrite(LED_4,LOW);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,HIGH);
        digitalWrite(LED_3,LOW);
        digitalWrite(LED_4,LOW);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,LOW);
        digitalWrite(LED_3,HIGH);
        digitalWrite(LED_4,LOW);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,LOW);
        digitalWrite(LED_3,LOW);
        digitalWrite(LED_4,HIGH);
        delay(WAIT_TIME_MS);
        digitalWrite(LED_1,LOW);
        digitalWrite(LED_2,LOW);
        digitalWrite(LED_3,LOW);
        delay(WAIT_TIME_MS);
    }

    return 1;
}