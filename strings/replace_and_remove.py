# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 10:22:00 2018

@author: I309535
"""

## removes each 'b' and replaces each 'a' by two 'd's.
def replace_and_remove(s):
   char_arr = list(s)
   for i in range(len(s)):
       if char_arr[i]=='b':
           char_arr[i]=''
       if char_arr[i]=='a':
           char_arr[i] = 'dd'
           
   return ''.join(char_arr)


s = 'acdbbca'
print replace_and_remove(s)