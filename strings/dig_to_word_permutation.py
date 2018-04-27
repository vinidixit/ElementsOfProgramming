# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:06:29 2018

@author: I309535
"""
dig_map = {'0':('a','b','c'),'1':('d','e','f'),'2':['g','h','i'],'3':['j','k','l']}
sequences=[]
def dig_to_word_perm(num_str,seq,sequences,dig_ind):
    if dig_ind == len(num_str):
        sequences.append(''.join(seq)) ## IMP*** : Cretae a "new" string and append "that" only.seq will get overwritten
        return
      
    chars = dig_map[num_str[dig_ind]]
    
    for char in chars:
        seq[dig_ind] = char
        dig_to_word_perm(num_str,seq,sequences,dig_ind+1)
    

num_str ='01'

seq=[None,None]
sequences = list()

dig_to_word_perm(num_str,seq,sequences,0) 
print sequences