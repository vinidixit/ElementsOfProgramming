# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 21:14:38 2018

@author: I309535
"""

def palindromic_permutation_test(string):
    d = dict()
    for i in range(len(string)):
        ch = string[i]
        if ch in d:
            d[ch]+=1
        else:
            d[ch] = 1
    
    ## **** odd count can't be more than 1
    odd_count = 0
    for ch in d:
        # if count is odd, not possible after 1
        if d[ch]%2 != 0 and odd_count == 1:
            return False
        else:
            odd_count+=1
    
    return True