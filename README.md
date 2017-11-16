# karaage-echo
Home assistant

## Dependency
- python2.7
- Julius
- OpenJtalk
- google-api-python-client

## Setup
### Hardware
- Raspberry Pi 2/3
- USB Microphone
- Speaker

### Software
Execute following commands for installing libraries:
```sh
$ sudo apt-get update
$ sudo pip install google-api-python-client
```

Setup Audio and Voice recognition(Julius). Refer to following page:  
http://karaage.hatenadiary.jp/entry/2015/08/24/073000

Setup OpenJtalk. Refer to following page(Japanese): 
http://karaage.hatenadiary.jp/entry/2016/07/22/073000

## Usage
### Speaking weather information
Execute following command:
```sh
$ python speak_bot.py -c weather -s
```

