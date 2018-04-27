# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:58:38 2018

@author: I309535
"""

## insert a character
# The method join() returns a string in which the string 
# elements of sequence have been joined by str separator.
' '.join('vini') # v i n i
'-'.join(('a','b','c')) # 'a-b-c'
'-'.join(['a','b','c']) # 'a-b-c'

## string to character
list('vini') # ['v','i','n','i']


## String operations
s = 'anffna'
# substring check
s.startswith('an') # True
s.endswith('na') # True

# search
s.index('f') # 2
s.index('fn') # 3
s.index('f',start=3)
# contains
'ff' in s # True


## String concatenation
# Since strings are immutable, + concat creates a new string each time
# So, an optimized way of concatenation is by using "join" operation in list of strings
s2 = ' '.join(('vini','dixit')) # 'vini dixit'

## delete an object
del s


## reverse a list
l=['rr', 'i', 'n', 'i']
l.reverse()  ## reverses the list

