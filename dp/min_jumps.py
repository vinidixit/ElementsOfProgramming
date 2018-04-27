# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 09:36:05 2018

@author: I309535
"""
# @param A : list of integers
# @return an integer
def jump(A):
    n = len(A)
    if n == 1:
        return 0 ## ****IMP input: [0]
    
    max_jumps = [0]*n
    max_jump_so_far = 0
    
    for i in range(n):
        max_jump_so_far = max(max_jump_so_far,A[i]+i)
        if max_jump_so_far < i:
            return -1
        
        if A[i]+i==A[i] and max_jump_so_far==i:
            return -1
            
        max_jumps[i] = max(max_jump_so_far, A[i]+i)
        
    
    min_jumps = 0
    ptr = n-2
    while ptr >= 0:
        cur_reach = ptr+1
        while ptr>=0 and max_jumps[ptr]>=cur_reach:
            ptr-=1
        min_jumps += 1        
        
    return min_jumps


A = [ 33, 21, 50, 0, 0, 46, 34, 3, 0, 12, 33, 0, 31, 37, 15, 17, 34, 18, 0, 4, 12, 41, 18, 35, 37, 34, 0, 47, 0, 39, 32, 49, 5, 41, 46, 26, 0, 2, 49, 35, 4, 19, 2, 27, 23, 49, 19, 38, 0, 33, 47, 1, 21, 36, 18, 33, 0, 1, 0, 39, 0, 22, 0, 9, 36, 45, 31, 4, 14, 48, 2, 33, 0, 39, 0, 37, 48, 44, 0, 11, 24, 16, 10, 23, 22, 41, 32, 14, 22, 16, 23, 38, 42, 16, 15, 0, 39, 23, 0, 42, 15, 25, 0, 41, 2, 48, 28 ]
print jump(A)