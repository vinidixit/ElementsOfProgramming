# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 22:17:32 2018

@author: I309535
"""

def next_permutation(perm):
    k = len(perm)-2
    while k >=0 and perm[k]>=perm[k+1]:
        k -=1
    if k<0:
        return [] # or reverse if need to find first minimum number
    
    i = len(perm)-1
    while i > k:
        if perm[k]<perm[i]:
            swap(perm,k,i)
            break
        i-=1
    
    perm[k+1:] = perm[k+1:][::-1]
    return perm
        
def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    

A = [1,0,6,4,5]
print next_permutation(A)
