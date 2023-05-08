# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 11:46:22 2019

@author: User
"""

from pycall import CallFile, Call, Application
call = Call('SIP/flowroute/18882223333')
action = Application('Playback', 'hello-world')

c = CallFile(call, action)
c.spool()