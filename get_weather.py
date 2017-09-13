#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import json

def get_weather():
    city = '230010'; # Nagoya
    json_url = 'http://weather.livedoor.com/forecast/webservice/json/v1' #API URL

    weather_text = u'%sの天気は%sだよ。'
    # temperature_text = u'%sの予想最高気温、%s度、予想最低気温、%s度だよ。'

    try:
        r = urllib2.urlopen('%s?city=%s' % (json_url, city) )
        obj = json.loads( unicode(r.read()) )

        title = obj['title']
        forecasts = obj['forecasts']

        # Today weather
        cast = forecasts[0]
        today_w_txt = weather_text % (cast['dateLabel'], cast['telop'])

        temperature = cast['temperature']

        if temperature['max']:
            today_t_max = unicode(temperature['max']['celsius']) + u'度'
        else:
            today_t_max = u'不明'

        if temperature['min']:
            today_t_min = unicode(temperature['min']['celsius']) + '度'
        else:
            today_t_min = u'不明'

        today_t_txt = u'今日の予想最高気温、' + today_t_max + u'。予想最低気温、' + today_t_min + u'だよ'

        # Tommorow weather
        cast = forecasts[1]
        # temperature = cast['temperature']
        tommorow_w_txt = weather_text % (cast['dateLabel'], cast['telop'])
        # tommorow_t_txt = temperature_text % (cast['dateLabel'], temperature['max']['celsius'], temperature['min']['celsius'])

        weather_str = today_w_txt + ' ' + tommorow_w_txt + ' ' + today_t_txt
        weather_str = weather_str.encode('utf-8')

    finally:
        r.close()

    return weather_str

if __name__ == "__main__":
    print(get_weather())
