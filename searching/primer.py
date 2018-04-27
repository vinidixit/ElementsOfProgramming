# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:41:00 2018

@author: I309535
"""

l = [('vini',9),('abhinaya',8),('abhigr',8),('avni',10)]

# sort on two keys
l.sort(key=lambda x:(x[1],x[0]),reverse=True)