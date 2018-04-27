# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 13:23:01 2018

@author: I309535
"""

class BinaryTreeNode:
    def __init__(self,val,left='END',right='END'):
        self.val = val
        self.left = left
        self.right = right
        
    def height(self):
        root = self
        if root.val == 'END':
            return 0
        
        lh,rh = 0,0
        if root.left !=None:
            lh = root.left.height()
        
        if root.right !=None:
            rh = root.right.height()
            
        return 1+ max(lh,rh)
    
    def level_order(self):
        from collections import deque
        queue = deque()
        root = self
        marker = '#'
        res = list()
        queue.append(root)
        queue.append('#')
                     
        while len(queue) >1:
            el = queue.popleft()
            if el == marker:
                queue.append('#')
                res.append('\n')
            elif el in ['(',')']:
                res.append(el)
            else:
                queue.append('(')
                if el == 'END':
                    res.append(str(el))
                else:
                    res.append(str(el.val))
                    queue.append(el.left)
                    queue.append(el.right)
                queue.append(')')    
                    
        return ' '.join(res)
    
    
class BinaryTree:
    def __init__(self,root):
        self.root = root
        
    def inorder(self):
        root = self.root
        stack = list()
        
        while True:
            while root != None:
                stack.append(root)
                root = root.left
                
            if len(stack)==0:
                break
            
            node = stack.pop()
            print node.val
            root = node.right
    
    
        
        
    
                    
                    
                    
                    
                
                
                
                
                
                
                
        
        
        
        
if __name__=='__main__':        
    root = BinaryTreeNode(5)
    node1 = BinaryTreeNode(3)
    node2 = BinaryTreeNode(1)
    node3 = BinaryTreeNode(4)
    
    node1.left = node2
    node1.right = node3
    root.left = node1
    
    node4 = BinaryTreeNode(8)
    node5 = BinaryTreeNode(6)
    node6 = BinaryTreeNode(10)
    
    node4.left = node5
    node4.right = node6
    root.right = node4
    
    root.inorder()
    print 'height:',root.height()
    
    print checkBalanceAndHeight(root)
    
    res= []
    search(BinaryTreeNode(6),root,[],res)
    print 'found :',len(res[0])
    for o in res[0]:
        print o.val
    
    def search_2(node_val,root,stack):
        if root == None:
            stack=[]
            return 
        
        if root.val==node_val:
            return 
        
        stack.append(root)
        search_2(node_val,root.left,stack)
        search_2(node_val,root.right,stack)
        
        