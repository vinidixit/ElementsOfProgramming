# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:21:02 2018

@author: I309535
"""

def compute_max_profit(a):
    max_profit = 0
    n = len(a)
    max_sell = a[n-1]
    
    for i in range(n-2,-1,-1):
        if a[i]<max_sell:
            max_profit = max(max_profit,max_sell-a[i])
        
        if a[i]>max_sell:
            # set max sell for previous buyers
            max_sell = a[i]
            
    return max_profit


a = (310,315, 275, 295, 260, 270, 290, 230, 255, 250)
print compute_max_profit(a)