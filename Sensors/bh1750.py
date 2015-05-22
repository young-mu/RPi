#!/usr/bin/python2
# coding:utf8

# NOTE:
# 1. python3 has no smbus module
# 2. wiringPiI2CRead() in wiringpi2 module fails to read the second byte

import time
import smbus

DEVICE = 0x23

# Continuously
CONT_LOW_RES_MODE = 0x13        # 4lx @ 16ms
CONT_HIGH_RES_MODE_1 = 0x10     # 1lx @ 120ms
CONT_HIGH_RES_MODE_2 = 0x11     # 0.5lx @ 120ms
# One time (low-power mode)
ONE_LOW_RES_MODE = 0x23         # 4lx @ 16ms
ONE_HIGH_RES_MODE_1 = 0x20      # llx @ 120ms
ONE_HIGH_RES_MODE_2 = 0x21      # 0.5lx @ 120ms

def initI2C():
    return smbus.SMBus(1)       # RPi2 uses i2c-1 bus

def cvtToNumber(data):
    assert type(data) == list
    return (((data[0] << 8) + data[1]) / 1.2)

def getLightCont(dev, i2cBus):
    try:
        data = i2cBus.read_i2c_block_data(dev, CONT_HIGH_RES_MODE_1, 2)
        return cvtToNumber(data)
    except Exception as err:
        return -1

def getLightOne(dev, i2cBus):
    try:
        data = i2cBus.read_i2c_block_data(dev, ONE_HIGH_RES_MODE_1, 2)
        return cvtToNumber(data)
    except Exception as err:
        return -1

def main():
    i2cBus = initI2C()
    light = getLightOne(DEVICE, i2cBus)
    if light != -1:
        print("光强（%dlx）" % light)
    else:
        print("Error: no sensor device")
        exit(1)

if __name__ == "__main__":
    main()
