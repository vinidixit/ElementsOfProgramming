# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 07:35:10 2018

@author: I309535
"""

def genPermutations(A):
    n = len(A)
    out = [None]*n
    permutations = list()
    genPermutationsAux(0,out,A,permutations)
    return permutations

def genPermutationsAux(level,out,A,permutations):
    if level==len(A):
        permutations.append(get_num(out,A))
        return
    
    for i in range(len(A)):
        if exists(out,i,level): ## putting level is important to give bound
            continue
        out[level] = i
        genPermutationsAux(level+1,out,A,permutations)
        
def exists(out, index, level):
    return index in out[:level]

def get_num(out,A):
    nums = [A[i] for i in out]
    return nums
    
def genPermutationsEditor(A):
    results = list()
    genPermutationsEditorAux(0,A,results)
    return results

def genPermutationsEditorAux(level,A,results):
    if level==len(A):
        results.append(list(A))
        return
    
    for j in range(level,len(A)):
        swap(A,level,j)
        genPermutationsEditorAux(level+1,A,results)
        swap(A,level,j) # to keep the final A unchanged
        
def genPermutationsInDup(A):
    results = list()
    genPermutationsInDupAux(0,A,results)
    return results

def genPermutationsInDupAux(level,A,results):
    if level==len(A):
        results.append(list(A))
        return 
    
    for j in range(level,len(A)):
        #print level,j
        if level!=j and A[level]==A[j]: ## no need to swap to same numbers
            continue
        swap(A,level,j)
        genPermutationsInDupAux(level+1,A,results)
        swap(A,level,j)
        
        
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
    
A = [2,2,1,1]
print genPermutationsInDup(A)
#print genPermutations(A)

#print genPermutationsEditor(A)
