# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:35:21 2018

@author: I309535
"""

def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l,r = 0,len(nums)-1
    while l < r:
        m = l + (r-l)/2
        if nums[m] < nums[r]:
            r = m
        else:
            l = m+1
    ## loop ends when l==r
    return nums[l]
    