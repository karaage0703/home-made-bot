#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shlex
import subprocess

from datetime import datetime

import urllib2
import json

import argparse

parser = argparse.ArgumentParser(
            prog='speak_bot.py',
            usage='speak bot',
            description='test',
            add_help=True,
            )

parser.add_argument('-c', '--command', help='select command')
parser.add_argument('-w', '--word', help='input word')
parser.add_argument('-f', '--file', help='read file txt')
parser.add_argument('-s', '--say', help='say or not', action='store_true')

def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/miku/miku.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

def get_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    return text

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
    args = parser.parse_args()

    word_txt = 'test'

    if args.command:
        if args.command == 'weather':
            word_txt = get_weather()
        if args.command == 'time':
            word_txt = get_datetime()

    if args.file:
        with open(args.file) as f:
            word_txt = f.read()
            word_txt = word_txt.replace('\n','')
            word_txt = word_txt.replace('\r','')

    if args.word:
        word_txt = args.word

    if args.say:
        print("talk")
        jtalk(word_txt)

    print(word_txt)
