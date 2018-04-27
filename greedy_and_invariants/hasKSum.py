# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 19:45:24 2018

@author: I309535
"""

def hasKSum(A, s,k):
    A.sort()
    return hasKSumHelper(A,s,k)

def hasKSumHelper(A,s,k):
    if k == 2:
        return hasTwoSum(A,s)
    
    for num in A:
        if hasKSumHelper(A,s-num,k-1):
            return True
    
    return False

def hasTwoSum(A,s):
    l,r = 0,len(A)-1
    
    while l < r:
        if A[l]+A[r]==s:
            return True
        
        if A[l]+A[r]<s:
            l+=1
        else:
            r-=1
            
    return False

A = [11,2,5,7,3]
A.sort()
print hasTwoSum(A,10)
print hasKSum(A,31,3)




