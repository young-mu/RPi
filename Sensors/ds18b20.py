#!/usr/bin/python

import wiringpi2 as GPIO

DQ = 0
IN = 0
OUT = 1
H = 1
L = 0
PULL_DN = 1
PULL_UP = 2

def initGPIO():
    GPIO.wiringPiSetup()
    GPIO.pullUpDnControl(DQ, PULL_UP)

def init18b20():
    GPIO.pinMode(DQ, OUT)
    GPIO.digitalWrite(DQ, H)
    GPIO.digitalWrite(DQ, L)
    GPIO.delayMicroseconds(480) # 480-960(us)
    GPIO.pinMode(DQ, IN)
    GPIO.delayMicroseconds(30) # 15-60(us)
    while True:
        if GPIO.digitalRead(DQ) == H:
            break;
    GPIO.delayMicroseconds(150) # 60-240(us)
    GPIO.digitalWrite(DQ, H)

def writeByte(data):
    GPIO.pinMode(DQ, OUT)
    for i in range(8):
        GPIO.digitalWrite(DQ, L)
        if data & (1 << i):
            GPIO.digitalWrite(DQ, H)
        else:
            GPIO.digitalWrite(DQ, L)
        GPIO.delayMicroseconds(30)

def readByte():
    data = 0;
    for i in range(8):
        GPIO.pinMode(DQ, OUT)
        GPIO.digitalWrite(DQ, L)
        GPIO.digitalWrite(DQ, H)
        GPIO.pinMode(DQ, IN)
        GPIO.delayMicroseconds(15)
        if GPIO.digitalRead(DQ) == H:
            data |= (1 << i);
        else:
            data &= ~(1 << i);
        GPIO.delayMicroseconds(30)
    return data

def getTemp():
    initGPIO()
    init18b20()
    writeByte(0xcc) # skip ROM
    writeByte(0x44) # convert temperature
    init18b20()
    writeByte(0xcc) # skip ROM
    writeByte(0xbe) # read scrachpad
    tempL = readByte()
    tempH = readByte()
    temp = ((tempH << 4) & 0xF0) + (tempL >> 4) + (tempL & 0x0F) / 16
    return temp

def main():
    temp = getTemp();
    print("Temperature is %f °C" % temp)

if __name__ == "__main__":
    main()
