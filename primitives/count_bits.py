# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 10:19:34 2018

@author: I309535
"""
# @param x : integer
# @return integer
def count_bits(x):
    num_bits = 0
    while x !=0:
        num_bits += x&1
        x = right_shift(x)
    return num_bits

def right_shift(x,shift=1):
    x = (x % 0x100000000) >> shift
    return x

#print (count_bits(-16))

print (right_shift(16,2))