# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 15:30:01 2018

@author: I309535
"""

def min_cover_window(A, values):
    
    dic = dict()
    i,j,n=0,0,len(A)

    while i< n and A[i] not in values:
        i += 1
    if i == n:
        return ''

    remaining = dict()
    for val in values:
        if val in remaining:
            remaining[val]+=1
        else:
            remaining[val] = 1
            
    j=i

    while j < n and len(remaining) > 0:
        if A[j] in values:
            if A[j] in remaining:
                if remaining[A[j]]==1:
                    del remaining[A[j]]
                else:
                    remaining[A[j]]-=1
                    
            if A[j] in dic:
                dic[A[j]]+=1
            else:
                dic[A[j]] = 1
        j += 1
        
    if len(remaining) > 0:
        return ''    
    ## found a cover in i:j+1
    
    min_cover = i,j-1
    print min_cover
    ## find minimum cover
    while True:
        while i < j:
            if A[i] in dic:
                if dic[A[i]] == 1:
                    break
                else:
                    dic[A[i]] -= 1
            i += 1
        
        if j-i<min_cover[1]-min_cover[0]:
            min_cover = i,j
            
        if j == n:
            break

        while j < n:# *********  WRONG : slide one by one to add new member
            if A[j] in values:
                dic[A[j]]+=1
            j+=1    
        
    return A[min_cover[0]:min_cover[1]+1]
            
A = 'ADOBECODEBANC' #'a' #[3,2,4,3,6,5,4,3,9] #'
values= 'ABC'#'ABC' #'ABC'#[5,4,3]
min_cover = min_cover_window(A,values)      
print min_cover
# 
               
    
##### ********** NOT WORKIgn : CHECK MIN_COVER_vr2