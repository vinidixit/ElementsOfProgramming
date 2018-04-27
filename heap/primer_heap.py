# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:39:07 2018

@author: I309535
"""

import heapq

A = [5, 7, 9, 1, 3]
## for min heap
#heapq.heapify(A)

## for max heap
heapq._heapify_max(A)

print A
print heapq.heappop(A)
print A

B = [('vini',1),('dixit',2)]
heapq.heapify(B)
print heapq.heappop(B)