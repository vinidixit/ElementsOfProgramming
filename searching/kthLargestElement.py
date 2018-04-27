# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:20:51 2018

@author: I309535
"""

def get_pivot(A,l,r):
    m = l+(r-l)/2
    cand = [(A[l],l),(A[m],m),(A[r],r)]
    cand.sort()
    return l#cand[1][1]
def swap(A,l,r):
    tmp = A[l]
    A[l]=A[r]
    A[r] = tmp
    
def partition(A,l,r):
    p = get_pivot(A,l,r)
    pivot_val = A[p]
    # swap
    swap(A,l,p)
    #A[l],A[p]=pivot_val,A[l]
    left,right = l+1,r
    
    while left<=right:
        while left <= r and A[left]<=pivot_val:
            left+=1
        while right>l and A[right]>pivot_val:
            right-=1
        
        if left<right:
            swap(A,left,right)
            left+=1
            right-=1
    # right > left and has lower number
    swap(A,l,right)
    return right

def kLargestElements(A,l,r,k):
    n = len(A)
    if l<=r:
        p = partition(A,l,r)            
        if p==n-k:
            return p
        if p>n-k:
            p = kLargestElements(A,l,p-1,k)
        else:
            p = kLargestElements(A,p+1,r,k)
    return p

import heapq
def kthLargestEl(A,k):
    l,r = 0,len(A)-1
    p = kLargestElements(A,l,r,k)
    heap = A[p:]
    
    # min heap
    heapq.heapify(heap)
    return heapq.heappop(heap)

def finMedian(A):
    n = len(A)
    k = n/2
 
    p = kLargestElements(A,0,n-1,k)
    print A
    print p,k
    return A[p] 
       
def quick_sort(A,l,r):
    
    if l >= r:
        return 
    print l,r
    p = partition(A,l,r)
    print l,p,r
    print A
    print A[p],'\n'
    quick_sort(A,l,p-1)
    quick_sort(A,p+1,r)
    
    
A = [3,4,1,2,5,7,6]
#quick_sort(A,0,len(A)-1)
#print A

#p = kLargestElements(A,0,len(A)-1,3)
#print A[p:]
#print kthLargestEl(A,3)

print finMedian(A)
        
