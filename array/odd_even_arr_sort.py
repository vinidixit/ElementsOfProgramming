# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:02:19 2018

@author: I309535
"""

"""
Sort array in the order of all even and then all odd numbers
Problem type : Partition
"""
def even_odd(a):
    next_even = 0
    next_odd = len(a)-1
    while next_even < next_odd:
        if a[next_even]%2==0:
            next_even += 1
        else:
            temp = a[next_even]
            a[next_even] = a[next_odd]
            a[next_odd] = temp
            next_odd -=1
            
    return a

print even_odd([1,2,3,4,5,6])