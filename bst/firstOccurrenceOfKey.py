# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:04:07 2018

@author: I309535
"""

def firstOccurrenceOfKey(root,key):
    subtree = root
    
    while subtree != None:
        if subtree.val < key:
            subtree = subtree.right
        elif subtree.val > key:
            subtree = subtree.left
        else:
            while subtree.left and subtree.left.val==key:
                subtree = subtree.left
            return subtree.val
        
    return None

from BST import create_bst
arr = [6,3,2,5,1,6,7]
root = create_bst(arr)
print firstOccurrenceOfKey(root,7)
