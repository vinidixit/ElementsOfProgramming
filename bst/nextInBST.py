# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:50:07 2018

@author: I309535
"""

def nextInBST(root, key):
    subtree = root
    firstSoFar = None
    
    while subtree != None:
        if subtree.val > key: # could be a prospective inorder successor
            firstSoFar = subtree
            subtree = subtree.left
        else:
            subtree = subtree.right    
            
    return firstSoFar.val

from BST import create_bst,BST

arr = [4,3,2,5,1,6,7]
root = create_bst(arr)
print nextInBST(root,6)
#bst = BST(root)
