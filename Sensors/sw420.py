#!/usr/bin/python

# Note:
# this is a python wrapper, the 3rd argument of wiringPiISR is an interrupt callback, if it's given a python function, it fails may be it's a bug for Python calling C

import os

def getVibration(sensitivity):
    os.system("./C/sw420 %s" % sensitivity);

def main():
    sensitivity = "medium"
    getVibration(sensitivity)

if __name__ == "__main__":
    main()
