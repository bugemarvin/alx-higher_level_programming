#!/usr/bin/python3
''' Script to fetch alx-intranet status
    Useage: package urllib
'''


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
