#!/usr/bin/python3

import requests
import io
url = 'https://raw.githubusercontent.com/shun-aky/1001_keyword/main/keyword.txt'
download = requests.get(url).content
print((download.decode('utf-8')))