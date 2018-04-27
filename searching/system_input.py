# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 18:27:36 2018

@author: I309535
"""

T = int(input())
result = []

for t in range(T):
    line = input()
    toks = line.split()
    A = [int(tok) for tok in toks]
    #res = binary_search(A)
    #result.append(res)
    print A