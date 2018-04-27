# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 19:18:55 2018

@author: I309535
"""

def min_cover_vr2(A,pattern):
    n = len(A)
    left = 0
    while left < n and A[left] not in pattern:
        left+=1
    
    if left == n:
        return ''
    remaining = dict()
    for val in pattern:
        if val in remaining:
            remaining[val]+=1
        else:
            remaining[val] = 1
    clone_remaining = remaining.copy()
        
    dic = dict()
    right = left
    while right < n and len(remaining)>0:
        if A[right] in remaining:
            if remaining[A[right]] == 1:
                del remaining[A[right]]
            else:
                remaining[A[right]] -=1
                
        if A[right] in pattern:
            if A[right] in dic:
                dic[A[right]]+=1
            else:
                dic[A[right]] = 1
        right += 1
        
    if len(remaining) >0:
        return ''
    
    min_cover = left,right-1
    print min_cover
    print 'remaining:',clone_remaining
    
    while True:
        while left < n: 
            if A[left] in dic:
                if dic[A[left]]==clone_remaining[A[left]]:
                    print 'breaking:',left,A[left],clone_remaining[A[left]]
                    break
                else:
                    dic[A[left]]-=1
            left +=1
        
        if right-1-left<min_cover[1]-min_cover[0]:
            min_cover = left,right-1
        
        print left,right,min_cover
        
        if right == n:
            break
        
        if A[right] in pattern:
            dic[A[right]]+=1
        right +=1
        
        print dic
        
        
    return A[min_cover[0]:min_cover[1]+1]

A = 'bbaac'#'ADOBECODEBANC'
p = 'aba'#'ABC'
print min_cover_vr2(A,p)
            
    
    
    
    
    
    
    