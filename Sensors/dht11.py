#!/usr/bin/python

# Note:
# Humidity should be monitored at an interval of 3 seconds at least
# Temperature has no such limitation

import wiringpi2 as GPIO
import signal

def initGPIO(pin):
    GPIO.wiringPiSetup()

def timeoutHandler(signum, frame):
    raise TimeoutError

def untilLow(pin):
    while True:
        if GPIO.digitalRead(pin) == 0:
            break;

def untilHigh(pin):
    while True:
        if GPIO.digitalRead(pin) == 1:
            break;

def readData(pin):
    hum = 0
    temp = 0
    crc = 0
    GPIO.pinMode(pin, 1)
    GPIO.digitalWrite(pin, 1)
    GPIO.digitalWrite(pin, 0)
    GPIO.delay(20)
    GPIO.digitalWrite(pin, 1)
    GPIO.pinMode(pin, 0)
    GPIO.delayMicroseconds(40)
    if GPIO.digitalRead(pin) == 0:
        untilHigh(pin)
        for i in range(16):
            hum <<= 1
            untilLow(pin)
            untilHigh(pin)
            GPIO.delayMicroseconds(28)
            hum += GPIO.digitalRead(pin)
        for i in range(16):
            temp <<= 1
            untilLow(pin)
            untilHigh(pin)
            GPIO.delayMicroseconds(28)
            temp += GPIO.digitalRead(pin)
        for i in range(8):
            crc <<= 1
            untilLow(pin)
            untilHigh(pin)
            GPIO.delayMicroseconds(28)
            crc += GPIO.digitalRead(pin)
        return [True, hum, temp, crc]
    else:
        return [False, hum, temp, crc]

def getTempAndHum(pin):
    initGPIO(pin)
    signal.signal(signal.SIGALRM, timeoutHandler)
    while True:
        try:
            signal.alarm(2) # avoid hang or no sensor
            [isSuccess, humdata, tempdata, crcdata] = readData(pin)
            signal.alarm(0)
        except TimeoutError:
            print("Error: no sensor device or hang")
            exit(1)
        if isSuccess == False: # avoid no sensor response
            continue
        humInt = (humdata & 0xFF00) >> 8
        humDec = (humdata & 0xFF)
        tempInt = (tempdata & 0xFF00) >> 8
        tempDec = (tempdata & 0xFF)
        crc = crcdata & 0xFF
        datasum = (humInt + humDec + tempInt + tempDec) & 0xFF
        if crc == datasum:
            return [humInt, tempInt]
        else:
            continue

def main():
    nGPIO = 0
    [humidity, temperature] = getTempAndHum(nGPIO)
    print("湿度（%.1f%%）" % (humidity))
    print("温度（%.1f°C）" % (temperature))

if __name__ == "__main__":
    main()
