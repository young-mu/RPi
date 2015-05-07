#!/usr/bin/python3
# coding:utf8

import subprocess as sp

def getTempOfCPU(type = 'C'):
    file = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = (float)(file.read()) / 1000
    file.close()
    if type == 'C':
        return cpu_temp
    elif type == 'F':
        return (1.8 * cpu_temp + 32)
    else:
        return 0

def getTempOfGPU(type = 'C'):
    ret = sp.getoutput("/opt/vc/bin/vcgencmd measure_temp")
    gpu_temp = (float)(ret.replace('temp=', '').replace('\'C', ''))
    if type == 'C':
        return gpu_temp
    elif type == 'F':
        return (1.8 * gpu_temp + 32)
    else:
        return 0

def main():
    print("CPU temp: " + str(getTempOfCPU('C')))
    print("GPU temp: " + str(getTempOfGPU('C')))

if __name__ == '__main__':
    main()

