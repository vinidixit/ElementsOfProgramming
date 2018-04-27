# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:09:28 2018

@author: I309535
"""

# @param A : integer
# @return an integer
def sqrt(self, A):
    if A < 2:
        return A
        
    l,r = 1,A
    res = l
    
    while l < r:
        m = l+(r-l)/2
        mid_square = m*m
        if mid_square == A:
            return m
        
        if mid_square < A:
            l = m+1 # m gives infinite loop
            res = max(res,m)
        else:
            r = m-1
            
    return res
