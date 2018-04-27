# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:31:02 2018

@author: I309535
"""

def combinations(A,string,result,ind,letter_map):
    if ind == len(A):
        result.append(string)
        return
    
    cur_digit = A[ind]
    letters = letter_map[cur_digit]
    
    for l in letters:
        combinations(A,string+l,result,ind+1,letter_map)
    
# @param A : string
# @return a list of strings
def letterCombinations(A):
    letter_map = {'1':'1','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':'0'}
    result = []
    combinations(A,'',result,0,letter_map)
    return result