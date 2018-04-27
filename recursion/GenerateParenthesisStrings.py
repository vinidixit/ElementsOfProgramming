# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 10:41:12 2018

@author: I309535
"""

def genParens(n):
    result = list()
    genParensHelper(0,0,'', n, result)
    return result

def genParensHelper(open_cnt, close_cnt, string, n, result):
    if open_cnt==n and open_cnt==close_cnt:
        result.append(string)
        
    if open_cnt < n:
        #string += '(' #### How could I do this silly mistake!! It was changing string content for next if block
        genParensHelper(open_cnt+1, close_cnt, string+'(', n, result)
        
    if close_cnt < open_cnt:
        #string += ')'
        genParensHelper(open_cnt, close_cnt+1, string+')', n, result)
        
        
        
print genParens(4)