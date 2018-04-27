# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 14:30:51 2018

@author: I309535
"""

def maxEventsPossible(events):
    events.sort(key=lambda x:(x[0],x[1]))