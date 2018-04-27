# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:46:51 2018

@author: I309535
"""

def is_palindrome(s):
    l = 0
    r = len(s)-1
    
    while l < r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True


s = 'anffna'
print is_palindrome(s)