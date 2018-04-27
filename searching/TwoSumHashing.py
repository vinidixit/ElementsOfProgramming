# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:55:13 2018

@author: I309535
"""

def twoSumHashing(self,A,target):
    dic = dict()
    n = len(A)
    
    for i in range(n):
        if A[i] in dic:
            dic[A[i]].append(i)
        else:
            dic[A[i]] = [i]
    
    min_index = [n,n]
    for num in A:
        num2 = target-num
        if num2 in dic and (num2!=num or len(dic[num2])>1):
            if num==num2:
                i = dic[num][0]+1
                j = dic[num][1]+1
            else:
                i = dic[num][0]+1
                j = dic[num2][0]+1
            
            if i > j:
                i,j = j,i
            
            if j < min_index[1]:
                min_index = [i,j]
            elif j == min_index[1] and i<min_index[0]:
                min_index = [i,j]
     
    return min_index if min_index[0]<n else ''