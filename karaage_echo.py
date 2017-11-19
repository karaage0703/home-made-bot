#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import subprocess
from time import sleep

from datetime import datetime

import get_weather as gw
import get_gcal_schedule as gc

host ='localhost'
port = 10500

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

def mic_on():
    cmd = "amixer sset Mic 50 -c 0"
    subprocess.call(cmd, shell=True)

def mic_off():
    cmd = "amixer sset Mic 0 -c 0"
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsock.connect((host, port))

    sf = clientsock.makefile('rb')

    while True:
        line = sf.readline().decode('utf-8')
        if line.find('WHYPO') != -1:
            print(line)
            if line.find(u'C1') != -1:
                mic_off()
                jtalk(gw.get_weather())
                sleep(5.0)
                mic_on()
            elif line.find(u'C2') != -1:
                mic_off()
                jtalk(get_datetime())
                sleep(5.0)
                mic_on()
            elif line.find(u'C3') != -1:
                mic_off()
                jtalk(gc.get_schedule())
                sleep(5.0)
                mic_on()
            elif line.find(u'CE') != -1:
                print("error command")
