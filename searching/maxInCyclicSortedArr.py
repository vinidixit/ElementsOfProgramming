# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 23:11:12 2018

@author: I309535
"""
"""
array is in strictly increasing order followed by strictly decreasing order.
"""
def largestNumInCyclicSortedArray(A):
    n = len(A)
    l,r = 0,n-1
    while l <= r:
        m = l+(r-l)/2
        
        if m>0 and m+1<n:
            if A[m-1]<A[m]>A[m+1]:
                return m
        elif m==0 and A[m]>A[m+1]:
                return m
        elif m==n-1 and A[m-1]<A[m]:
                return m
        
        if A[m-1]<A[m]: ## increasing seq
            l = m+1
        else: # decreasing seq
            r = m-1
            
    return -1

def largestNumInCyclicSortedArray_vr2(A):
    n = len(A)
    l,r = 0,n-1
    while l < r:
        m = l+(r-l)/2
        
        if m>0 and m+1<n:
            if A[m-1]<A[m]>A[m+1]:
                return m
        elif m==0 and A[m]>A[m+1]:
                return m
        elif m==n-1 and A[m-1]<A[m]:
                return m
        
        if A[m-1]<A[m]: ## increasing seq
            l = m
        else: # decreasing seq
            r = m
    
    # loop ends at l==r
    
    return l

A = [4,5,6,9,8,5,4,3,2,1,-2,-3,-5]
print A[largestNumInCyclicSortedArray_vr2(A)]

#### WORKING