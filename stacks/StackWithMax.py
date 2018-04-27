# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:15:27 2018

@author: I309535
"""

class Stack:
    def __init__(self):
        self.__elements = list()
        self.__max_with_counts = list() #list of pairs
    
    def empty(self):
        return len(self.__elements)==0
    
    def push(self,el):
        self.__elements.add(el)
        if self.empty():
            self.__max_with_counts.append([el,1])
        else:
            cur_max_el = self.__max_with_counts[-1][0]
            if cur_max_el==el:
                self.__max_with_counts[-1][1]+=1
            else:
                self.__max_with_counts.append([el,1])
                
    def pop(self):
        if self.empty():
            print 'Stack is empty.'
            return
        
        el = self.__elements[-1]
        self.__elements = self.__elements[0:-1]
        
        cur_max_el = self.__max_with_counts[-1][0]
        if el ==cur_max_el:
            self.__max_with_counts[-1][1]-=1
            if self.__max_with_counts[-1][1]==0:
                self.__max_with_counts[-1][1]=self.__max_with_counts[0:-1]
            
        return el
            
            
st = Stack()