# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 20:52:08 2018

@author: I309535
"""
import numpy as np
"""
Contact list problem: store unique names, 
ordering of words in contact does not matter
"""
class Item:
    def __init__(self,names):
        # only tuple is hashbale
        self.names = tuple(np.unique(names))
    
    def __eq__(self, other):
        if isinstance(other, Item):
            ## set equality is irrespective of order and is elementwise
            return set(other.names)==set(self.names)
        return False
    
    def __hash__(self):
        return hash(self.names)
    
        
s = set()
it1 = Item(('vini','dixit','dixit'))
it2 = Item(('vini','dixit'))

s.add(it1)
s.add(it2)

for it in s:
    print it.names

print Item(('vini','dixit')) in s

### **** initialize dictionary with a list of keys and default/initial values
default_value = 'xyz'
nonempty_dict = dict.fromkeys(['apple','ball'],default_value)

import string
digits = range(1,27)
letters = list(string.ascii_uppercase[:27])
## ****** initialize dictionary with list of keys and values
dig_letter_map = dict(zip(digits,letters))

