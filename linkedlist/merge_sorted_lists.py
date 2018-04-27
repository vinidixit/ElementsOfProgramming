# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 17:48:51 2018

@author: I309535
"""
from ListNode import ListNode

def merge_sorted_lists(head1,head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    
    dummy_head = ListNode('S')
    current = dummy_head
    p1 = head1
    p2 = head2
    
    while p1 !=None and p2!=None:
        if p1.data<=p2.data:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        
        current = current.next
    
    ## Append the remaining
    current.next = p1 if p1!=None else p2
        
    return dummy_head.next # ptr is at last node ******IMP : to take a navigating variable

head1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(6)
node4 = ListNode(8)
node5 = ListNode(10)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head2 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(5)
node4 = ListNode(7)
node5 = ListNode(9)

head2.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

res = merge_sorted_lists(head1,head2)
#res.show()

head1.show()
print '\n'

#head2.show()