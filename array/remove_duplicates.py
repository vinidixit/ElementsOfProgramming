# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 12:45:01 2018

@author: I309535
"""

def delete_duplicates(arr):
    n = len(arr)
    if n == 0:
        return
    
    prev,emp = arr[0],None
    for i in range(1,n):
        cur = arr[i]
        if cur==prev:
            arr[i] = 0
            if emp==None:
                emp=i
        elif emp!=None:
            print emp
            arr[emp] = cur
            arr[i] = 0
            emp+=1
        prev = cur
     
def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    
    
A = [2,3,5,5,5,7,11,11,11,13]
delete_duplicates(A)
print A