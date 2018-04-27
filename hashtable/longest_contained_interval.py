# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:34:59 2018

@author: I309535
"""

def longestContainedInterval(A):
    unprocessed_set = set(A)
    maxInterval = 0
    
    while len(unprocessed_set)>0:
        cur = unprocessed_set.pop()
        lower = cur-1
        while lower in unprocessed_set:
            unprocessed_set.remove(lower)
            lower-=1
        
        upper = cur+1
        while upper in unprocessed_set:
            unprocessed_set.remove(upper)
            upper+=1
        print cur,lower,upper,unprocessed_set,'\n'    
        maxInterval = max(maxInterval,upper-lower-1)
    return maxInterval

print longestContainedInterval([3,-2,7,9,8,1,2,0,-1,5,8])