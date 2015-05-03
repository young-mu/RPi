#!/usr/bin/python3
# coding:utf8

import json
import urllib.request

kelvin = 273.15
apiWeather = "http://api.openweathermap.org/data/2.5/weather"
apiForecast = "http://api.openweathermap.org/data/2.5/forecast"
appid = "c9a0753615c01095701a37f97ae76583"

def getMostEle(mylist):
    mylist_with_count = map(lambda x: (mylist.count(x), x), mylist)
    mylist_most_count = max(mylist_with_count)
    return mylist_most_count[1]

def getWeatherInner(city):
    try:
        weather_host = apiWeather + "?q=" + city + "&appid=" + appid
        urlfile = urllib.request.urlopen(weather_host)
        html = urlfile.read()
        html = html.decode('utf8', 'strict')
        weather_info = json.loads(html)
        desc = weather_info['weather'][0]['main']
        temp = round((weather_info['main']['temp'] - kelvin), 2)
        humidity = weather_info['main']['humidity']
        ret_dict = {'desc':desc, 'temp':temp, 'humidity':humidity}
        return ret_dict
    except Exception as err:
        return False

def getWeather(city):
    while True:
        ret = getWeatherInner(city)
        if ret:
            return ret

def getForecastInner(city):
    try:
        forecast_host = apiForecast + "?q=" + city + "&appid=" + appid
        urlfile = urllib.request.urlopen(forecast_host)
        html = urlfile.read()
        html = html.decode('utf8', 'strict')
        forecast_info = json.loads(html)
        forecast_list = forecast_info['list']
        forecast_detail = []
        for i in range(len(forecast_list)):
            time = forecast_list[i]['dt_txt']
            desc = forecast_list[i]['weather'][0]['main']
            temp = round((forecast_list[i]['main']['temp'] - kelvin), 2)
            item = (time, desc, temp)
            forecast_detail.append(item)
        # merge into 4 days (everyday has 8 timepoints)
        forecasts = []
        for i in range(4):
            alldescs = []
            alltemps = []
            for j in range(8):
                alldescs.append(forecast_detail[i*8+j][1])
                alltemps.append(forecast_detail[i*8+j][2])
            descs = getMostEle(alldescs)
            mintemp = min(alltemps)
            maxtemp = max(alltemps)
            avetemp = round(sum(alltemps)/len(alltemps), 2)
            oneday = (descs, mintemp, maxtemp, avetemp)
            forecasts.append(oneday)
        return forecasts
    except Exception as err:
        return False

def getForecast(city):
    while True:
        ret = getForecastInner(city)
        if ret:
            return ret

def main():
    weather = getWeather('shanghai')
    print("weather: %s temperature: %.2f humidity: %d" % (weather['desc'], weather['temp'], weather['humidity']))
    forecasts = getForecast('shanghai')
    for i in range(len(forecasts)):
        desc = forecasts[i][0]
        mintemp = int(round(forecasts[i][1]))
        maxtemp = int(round(forecasts[i][2]))
        print("(day" + str(i+1) + ") " + "weather: %-8s temperature:%d-%d" % (desc, mintemp, maxtemp))

if __name__ == "__main__":
    main()
