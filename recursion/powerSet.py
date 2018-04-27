# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:19:27 2018

@author: I309535
"""

def genPowerSet(A, k=None):
    subsets = list()
    out = [None]*len(A)
    genPowerSetAux(0,A,subsets,out,0,k)
    return subsets

def genPowerSetAux(level,A,subsets,out,cur_ind, k):
    #if 0 < level <= len(A):
    if k==None and level == 0:
        subsets.append(list())
    else:
        if k==None or level==k:
            subsets.append(list(out[:level]))
    
    if (k and level >= k) or level==len(A):
        return
    
    for i in range(cur_ind,len(A)):
        out[level] = A[i]    
        genPowerSetAux(level+1,A,subsets,out,i+1,k)
                
A = [1,2,3,4]

print genPowerSet(A,2)