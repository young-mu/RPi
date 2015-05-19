#!/usr/bin/python3
# coding:utf8

import json
import urllib.request
import socket

timeout = 1
kelvin = 273.15
apiWeather = "http://api.openweathermap.org/data/2.5/weather"
apiForecast = "http://api.openweathermap.org/data/2.5/forecast/daily"
appid = "c9a0753615c01095701a37f97ae76583"

def getWeatherInner(city):
    try:
        weather_host = apiWeather + "?q=" + city + "&appid=" + appid
        socket.setdefaulttimeout(timeout)
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
    for i in range(5):
        weather = getWeatherInner(city)
        if weather is False:
            continue
        else:
            return weather
     return False

def getForecastInner(city):
    try:
        forecast_host = apiForecast + "?q=" + city + "&appid=" + appid
        socket.setdefaulttimeout(timeout)
        urlfile = urllib.request.urlopen(forecast_host)
        html = urlfile.read()
        html = html.decode('utf8', 'strict')
        forecast_info = json.loads(html)
        forecast_list = forecast_info['list']
        forecasts = []
        for i in range(len(forecast_list)):
            desc = forecast_list[i]['weather'][0]['main']
            mintemp = round((forecast_list[i]['temp']['min'] - kelvin), 2)
            maxtemp = round((forecast_list[i]['temp']['max'] - kelvin), 2)
            item = (desc, mintemp, maxtemp)
            forecasts.append(item)
        return forecasts
    except Exception as err:
        return False

def getForecast(city):
    for i in range(5):
        forecast = getForecastInner(city)
        if forecast is False:
            continue
        else:
            return forecast
    return False


def main():
    weather = getWeather('shanghai')
    if weather is not False:
        print("天气:%s 温度:%.2f 湿度:%d" % (weather['desc'], weather['temp'], weather['humidity']))
    else:
        print("Get weather failed! (timeout)")
    forecasts = getForecast('shanghai')
    if forecasts is not False:
        for i in range(len(forecasts)):
            desc = forecasts[i][0]
            mintemp = int(round(forecasts[i][1]))
            maxtemp = int(round(forecasts[i][2]))
            print("(第" + str(i+1) + "天) " + "天气:%-8s 温度:%d-%d" % (desc, mintemp, maxtemp))
    else:
        print("Get forecast failed! (timeout)")

if __name__ == "__main__":
    main()
