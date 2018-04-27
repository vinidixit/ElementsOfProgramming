# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:19:23 2018

@author: I309535
"""

def genPalindromicDecomp(num_str):
    result = list()
    genPalindromicDecompAux(num_str,0,[],result)
    return result

def genPalindromicDecompAux(num_str,start,decomp,result):
    if start == len(num_str):
        result.append(list(decomp))
        return    
    
    for end in range(start+1,len(num_str)+1):
        prefix = num_str[start:end]
        if isPalindrome(num_str,start,end-1):
            """
            # prev partition
            if len(result)>0:
                decomp = result[-1][:start]
            """
            decomp.append(prefix)
            genPalindromicDecompAux(num_str,end,decomp,result)
            # reset for next branch
            decomp = decomp[:-1] # clear the list
            
def isPalindrome(num_str,start,end):
    while start < end:
        if num_str[start]!=num_str[end]:
            return False
        start+=1
        end-=1
    
    return True

print genPalindromicDecomp('02044')