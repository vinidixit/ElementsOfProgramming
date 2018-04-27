# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:31:37 2018

@author: I309535
"""
"""
single underscore is for protected member of variable: can be only used by inheriting class
double underscore is for private variables: can be used by only class
"""
from ListNode import ListNode

class LinkedList:
    def __init__(self,data):
        node = ListNode(data)
        self.__head = node
        self.__tail = node
        
    def add(self,data):
        node = ListNode(data)
        self.__tail.set_next(node)
        self.__tail = node
    
    def get_data(self):
        return self.__head.get_data()
    
    def get_next(self):
        return self.__head.get_next();
            
    def show(self):
        l = self
        while l!= None:
            print l.get_data()
            l=l.get_next()
        
if __name__== "__main__":
    ll = LinkedList(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    
    ll.show()