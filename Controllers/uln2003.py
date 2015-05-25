#!/usr/bin/python

# NOTE:
# step motor's name is 28byj48, uln2003 is driver module's name

import sys
import wiringpi2 as GPIO

nGPIOs = [0, 1, 2, 3]

CW = 0
CW_seq = list(range(4))
CW_seq[0] = [1, 0, 0, 0]
CW_seq[1] = [0, 1, 0, 0]
CW_seq[2] = [0, 0, 1, 0]
CW_seq[3] = [0, 0, 0, 1]

CCW = 1
CCW_seq = list(range(4))
CCW_seq[0] = [0, 0, 0, 1]
CCW_seq[1] = [0, 0, 1, 0]
CCW_seq[2] = [0, 1, 0, 0]
CCW_seq[3] = [1, 0, 0, 0]

def prUsage():
    print("Usage:")
    print("./uln2003.py [CW|CWW] delay(2-20)");
    sys.exit(1)

def initGPIO(nGPIOs):
    GPIO.wiringPiSetup()
    for pin in nGPIOs:
        GPIO.pinMode(pin, 1)

def rotate(nGPIOs, seq, delay):
    while True:
        for i in range(4):
            for j in range(4):
                GPIO.digitalWrite(nGPIOs[j], seq[i][j])
            GPIO.delay(delay)

def start(nGPIOs, direction, delay):
    if direction == CW:
        print("Clockwise")
        rotate(nGPIOs, CW_seq, delay)
    elif direction == CCW:
        print("CounterClockwise")
        rotate(nGPIOs, CCW_seq, delay)

def stop(nGPIOs):
    for pin in nGPIOs:
        GPIO.digitalWrite(pin, 0)

def main():
    initGPIO(nGPIOs)
    if len(sys.argv) != 3:
        prUsage()
    else:
        delay = int(sys.argv[2])
        if delay < 2 or delay > 20:
            prUsage()
        if sys.argv[1] == "CW":
            start(nGPIOs, CW, delay);
        elif sys.argv[1] == "CCW":
            start(nGPIOs, CCW, delay);
        else:
            prUsage()

if __name__ == "__main__":
    main()
