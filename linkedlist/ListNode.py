# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 07:48:09 2018

@author: I309535
"""

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None # when no next, it takes implicit next() method and throws an error for tail's next
         
    def show(self):
        node = self
        while node != None:
            print node.data
            node = node.next
"""      
 basic list operations
"""
# Search for a key
def search(node,key):
    while node != None and node.data!=key:
        node = node.next
    
    return node

# Insert a new node after a specified node
def insert_after(node,new_node):
    new_node.next = node.next
    node.next = new_node

# Delete a node
def delete(node):
    node.next = node.next.next
    
if __name__=='__main__':
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    insert_after(head,node2)
    insert_after(node2,node3)
    insert_after(node3,node4)
    
    search_node = search(head,3)
    if search_node==None:
        print 'search not found.'
    else:
        print 'found:',search_node.data
      
    head.show()
    head.show()
    head.show()