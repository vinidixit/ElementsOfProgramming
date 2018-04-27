# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 10:03:03 2018

@author: I309535
"""
from BinaryTree import BinaryTreeNode

class BST:
    
    def __init__(self,root):
        self.root = root
        
    def contains(self,data):
        root = self.root
        return self.aux_contains(root,data)
        
    def aux_contains(self,root,data):
        if root != None:
            if root.val == data:
                return True
            
            ls = self.aux_contains(root.left,data)
            rs = self.aux_contains(root.right,data)
            if ls or rs:
                return True
        return False
    
def create_bst(arr):
    arr.sort()
    return aux_create_bst(arr,0,len(arr)-1)
    
def aux_create_bst(arr,l,r):
    if l > r:
        return None
    m = l + (r-l)/2
    
    root = BinaryTreeNode(arr[m])
    root.left = aux_create_bst(arr,l,m-1)
    
    root.right = aux_create_bst(arr,m+1,r)
    return root

# @param A : root node of tree
# @param B : integer
# @return an integer
def t2Sum(A, B):
    min_stack = list([A])
    max_stack = list([A])
    
    while len(min_stack)!=0 and len(max_stack)!=0:
        cur_sum = min_stack[-1].val+max_stack[-1].val
        
        if cur_sum==B:
            return 1
            
        if cur_sum < B: #increase: by pushing right from min_stack
            cur_node = min_stack.pop().right
            while cur_node!=None:
                min_stack.append(cur_node)
                cur_node = cur_node.left
        else:  # decrease: by pushing left from max stack
            cur_node = min_stack.pop().left
            while cur_node!=None:
                min_stack.append(cur_node)
                cur_node = cur_node.right
                
    return 0

def lca_bst(root,node1,node2):
    if root==None:
        return None
    
    # when they are at same branch
    if root.val in [node1.val,node2.val]:
        return root
    
    is_ls = node1.val<=root.val and node2.val<=root.val
    is_rs = node1.val>root.val and node2.val>root.val
    
    ## nodes are in different sides of the root
    if not is_ls and not is_rs:
        return root
    
    if is_ls:
        lca = lca_bst(root.left,node1,node2)
        if lca != None:
            return lca
    if is_rs:
        lca = lca_bst(root.right,node1,node2)
        if lca != None:
            return lca

    
arr = [4,3,2,5,1,6,7]
root = create_bst(arr)
bst = BST(root)

print bst.root.level_order()

search_el = 6
print '\nBST contains:'

print bst.contains(10)

print t2Sum(bst.root,21)


    
lca = lca_bst(root,BinaryTreeNode(5),BinaryTreeNode(1))    
print 'lca :',lca.val    
        
