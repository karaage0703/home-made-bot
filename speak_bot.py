#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

from datetime import datetime

import argparse
import get_weather as gw
import get_gcal_schedule as gc

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

if __name__ == "__main__":
    args = parser.parse_args()

    word_txt = 'test'

    if args.command:
        if args.command == 'weather':
            word_txt = gw.get_weather()
        if args.command == 'time':
            word_txt = get_datetime()
        if args.command == 'schedule':
            word_txt = gc.get_schedule()

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
