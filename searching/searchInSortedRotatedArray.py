# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:47:39 2018

@author: I309535
"""


def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    l,r = 0, len(nums)-1
    
    while l <= r:
        m = l + (r-l)/2
        if nums[m] == target:
            return m
        # handle array of size 2
        if m == l:
            if nums[l]==target:
                return l
            if nums[r]==target:
                return r
            return -1
        
        ## solution for array of minimum length 3
        ## Overlap: 11,4,6
        if nums[l] > nums[m] < nums[r]:
            if target > nums[m]: ## can be in either side
                if target >= nums[l]: ## Important equality
                    r= m-1
                else:
                    l = m+1
            else:
                r = m-1
        ## Overlap: 10,11,1
        elif nums[l]<nums[m]>nums[r]:
            if target > nums[m]:
                l = m+1
            else:
                if target>=nums[l]: ## Important equality
                    r = m-1
                else:
                    l = m+1
        ## increasing
        elif nums[l]<nums[m]<nums[r]:
            if nums[m]>target:
                r = m-1
            else:
                l = m+1
        else: ## decreasing
            if nums[m] > target:
                l = m+1
            else:
                r = m-1
            
    return -1