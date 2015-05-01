#!/usr/bin/python
# coding:utf8

import json
import urllib2

# Ref: http://www.pm25.in/api_doc
apiAQI = 'http://www.pm25.in/api/querys/only_aqi.json'
city = 'shanghai'
token = '5j1znBVAsnSf5xQyNQyq'
AQI_host = apiAQI + '?city=' + city + '&token=' + token

SH_stations = ('putuo', 'changning', 'hongkou', 'xuhui', 'yangpu', 'qingpu', 'jingan', 'chuansha', 'pudong', 'zhangjiang', 'shanghai')

def getAQI():
    urlfile = urllib2.urlopen(AQI_host)
    html = urlfile.read()
    AQIs = json.loads(html)
    AQI_dict = {}
    for i in range(len(AQIs)):
        AQI_dict[SH_stations[i]] = AQIs[i]['aqi']
    return AQI_dict

def main():
    AQIs = getAQI()
    print("上海: " + str(AQIs['shanghai']))
    print("浦东: " + str(AQIs['pudong']))
    print("杨浦: " + str(AQIs['yangpu']))
    print("虹口: " + str(AQIs['hongkou']))
    print("徐汇: " + str(AQIs['xuhui']))

if __name__ == "__main__":
    main()
