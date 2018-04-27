# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:07:24 2018

@author: I309535
"""
"""
**** REVERSE INORDER : RIGHT->root->left
"""
def kLargestInBST(root, k):
    subtree = root
    stack = list()
    #stack.append(subtree)
    while k > 0:
        while subtree:
            stack.append(subtree)
            subtree = subtree.right
        
        if len(stack)>0:
            kmax = stack.pop()
            print k,':',kmax.val
            k -= 1
            subtree = kmax.left
            
                
from BST import create_bst
arr = [4,3,2,5,1,6,7,8,9,10,23,21]
root = create_bst(arr)
#root.inorder()

kLargestInBST(root,4)

                
    