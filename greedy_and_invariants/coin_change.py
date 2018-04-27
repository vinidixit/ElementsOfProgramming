# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 12:18:23 2018

@author: I309535
"""

def changeMaking(coins,cents):
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if cents == 0:
            break
        num_coins += cents/coin
        cents %= coin
    return num_coins

coins = [1,5,10,25,50,100]
print changeMaking(coins,505)