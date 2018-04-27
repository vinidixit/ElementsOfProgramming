# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:48:38 2018

@author: I309535
"""

def findMaxInAscendingDescendingArr(A):
    l,r = 0, len(A)-1
    while l <= r:
        m = l+(r-l)/2
        left_check = False
        if m >0:
            if A[m-1]<A[m]:
                left_check = True
        else:
            left_check = True
        
        right_check = False
        if m < len(A)-2:
            if A[m]>A[m+1]:
                right_check = True
        else:
            right_check = True
            
        if left_check and right_check:
            return m
        
        if A[m-1]<A[m]:
            l = m
        else:
            r = m-1
        if A[m] > A[m+1]:
            r = m
        else:
            l = m+1
        
        
A = [4,5,6,5,4,3,2]
print A[findMaxInAscendingDescendingArr(A)]
