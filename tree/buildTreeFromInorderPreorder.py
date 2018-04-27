# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 21:28:20 2018

@author: I309535
"""
from BinaryTree import BinaryTreeNode

def build_tree(preorder, inorder):
    return build_tree_helper(preorder,inorder,0,len(inorder)-1)

build_tree.preindex = 0                             
def build_tree_helper(preorder,inorder,in_start,in_end):
    
    if (in_start > in_end):
        return None
 
    # Pich current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = BinaryTreeNode(preorder[build_tree.preindex])
    build_tree.preindex += 1
 
    # If this node has no children then return
    if in_start == in_end :
        return tNode
 
    # Else find the index of this node in Inorder traversal
    inIndex = search(inorder,in_start,in_end, tNode.val)
     
    # Using index in Inorder Traversal, construct left 
    # and right subtrees
    tNode.left = build_tree_helper(preorder,inorder,in_start, inIndex-1)
    tNode.right = build_tree_helper(preorder, inorder, inIndex+1, in_end)
 
    return tNode
    """
    if in_start>in_end:
        return None
    
    root = BinaryTreeNode(preorder[build_tree.preindex])
    build_tree.preindex+=1
    
    if in_start==in_end:
        return root
    
    p = search(inorder,in_start,in_end,root.val)
    root.left = build_tree_helper(preorder,inorder,in_start,p-1)
    root.right = build_tree_helper(preorder,inorder,p+1,in_end)
    return root
    """
def search(inorder, start,end, num):
    for i in range(start,end+1):
        if num==inorder[i]:
            return i
    

inorder = list('FBAEHCDIG')
preorder = list('HBFEACDGI')

tree = build_tree(preorder,inorder)

print tree.level_order()