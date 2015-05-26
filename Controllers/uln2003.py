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
    print("1) ./uln2003.py start direction=[0|1] delay=[2-20]");
    print("2) ./uln2003.py stop");
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
        rotate(nGPIOs, CW_seq, delay)
    elif direction == CCW:
        rotate(nGPIOs, CCW_seq, delay)

def stop(nGPIOs):
    for pin in nGPIOs:
        GPIO.digitalWrite(pin, 0)

def main():
    initGPIO(nGPIOs)
    if len(sys.argv) != 2 and len(sys.argv) != 4:
        prUsage()
    elif len(sys.argv) == 2 and sys.argv[1] == "stop":
        stop(nGPIOs)
    elif len(sys.argv) == 4 and sys.argv[1] == "start":
        direction = int(sys.argv[2])
        if direction != 0 and direction != 1:
            prUsage()
        delay = int(sys.argv[3])
        if delay < 2 or delay > 20:
            prUsage()
        start(nGPIOs, direction, delay);
    else:
        prUsage()

if __name__ == "__main__":
    main()
