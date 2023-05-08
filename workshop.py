# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 18:09:58 2021

@author: User
"""

import urllib
import webbrowser
weburl=urllib.request.urlopen('https://www.ted.com/')
html=weburl.read()
data=weburl.getcode()
url=weburl.geturl()
hd=weburl.headers
inf=weburl.info()
print('The url is', url)
print('HTTP status code is:', data)
print("headers returned \n",hd)
print("The info() returned : \n",inf)
print("Now opening Url" ,url)
webbrowser.open_new(url)