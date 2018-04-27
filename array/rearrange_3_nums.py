# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:22:51 2018

@author: I309535
"""
"""
Write a program that takes an array A and an index i into A,
and rearranges the elementssuch that all elements less than
A[i] (the "pivot") appear first, followed by elements equal
to the pivot, followed by elements greater than the pivot.
"""

def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    return a

def rearrange_arr(a,i):
    l,m,r=0,0,len(a)-1
    pivot = a[i]
    
    while m <= r:
        if a[m]<pivot:
            a = swap(a,l,m)
            l+=1
            
        elif a[m]==pivot:
            m += 1
        else: #condition of r
            a = swap(a,m,r)
            r -=1
    return a


a = [2,0,1,1,0,1,0]
print rearrange_arr(a,1)