# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:44:59 2018

@author: I309535
"""
import heapq
import numpy as np

def topKLongestStrings(A,k):
    heap = []
    
    # in a stream
    for string in A:
        heap.append((len(string),string))
        heapq.heapify(heap)
        
        if len(heap) > k:
            heapq.heappop(heap)
    
    return np.array(heap)[:,1]

print topKLongestStrings(['vini','alicia','vini dixit','anvesh d.'],2)
    
    