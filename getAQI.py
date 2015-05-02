#!/usr/bin/python
# coding:utf8

import json
import urllib2

# Ref: http://www.pm25.in/api_doc
apiAQI = 'http://www.pm25.in/api/querys/only_aqi.json'
city = 'shanghai'
token = '5j1znBVAsnSf5xQyNQyq'
AQI_host = apiAQI + '?city=' + city + '&token=' + token

def getAQI():
    urlfile = urllib2.urlopen(AQI_host)
    html = urlfile.read()
    AQIs = json.loads(html)
    stations_name = []
    stations_code = []
    index = []
    quality = []
    AQI_dict = {}
    for i in range(len(AQIs)):
        stations_code.append(AQIs[i]['station_code'])
        stations_name.append(AQIs[i]['position_name'])
        index.append(AQIs[i]['aqi'])
        quality.append(AQIs[i]['quality'])
        if (stations_name[i] != None):
            AQI_dict[stations_code[i]] = (stations_name[i], index[i], quality[i])
    return AQI_dict

def main():
    AQIs = getAQI()
    AQIlist = AQIs.items()
    assert type(AQIs) == dict
    assert type(AQIlist) == list
    for i in range(len(AQIlist)):
        print("%s %3d(%s)  %s" % (AQIlist[i][0], AQIlist[i][1][1], AQIlist[i][1][2], AQIlist[i][1][0]))
    print("浦东: %d" % AQIs['1149A'][1])

if __name__ == "__main__":
    main()
