#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <wiringPi.h>

#define nGPIO           0

static volatile int globalCounter;

void countHandler(void)
{
    globalCounter++;
}

void prUsage(void)
{
    printf("Usage:\n");
    printf("sudo ./sw420 [sensitivity=high|medium|low]\n");
    exit(1);
}

int main(int argc, const char *argv[])
{
    int threshold;
    if (argc == 2) {
        if (strcmp(argv[1], "high") == 0) {
            threshold = 1;
        } else if (strcmp(argv[1], "medium") == 0) {
            threshold = 5;
        } else if (strcmp(argv[1], "low") == 0) {
            threshold = 10;
        } else {
            prUsage();
        }
    } else {
        prUsage();
    }

    wiringPiSetup();
    pinMode(nGPIO, INPUT);
    wiringPiISR(nGPIO, INT_EDGE_RISING, countHandler);
    if (digitalRead(nGPIO) == LOW) {
        printf("working ...\n");
        fflush(stdout);
    } else {
        printf("NOT working, EXIT!\n");
        exit(1);
    }

    while (1) {
        if (globalCounter >= threshold) {
            globalCounter = 0;
            printf("vibration triggered\n");
        }
    }

    return 0;
}
