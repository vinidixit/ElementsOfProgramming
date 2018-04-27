# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:55:47 2018

@author: I309535
"""

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
print queue