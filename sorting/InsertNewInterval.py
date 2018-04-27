# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:18:33 2018

@author: I309535
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def is_overlapping(self,intervals,l,newInterval):
        cur_s = intervals[l].start
        cur_e = intervals[l].end
        new_s = newInterval.start
        new_e = newInterval.end
        return new_s<=cur_s<=new_e or new_s<=cur_e<=new_e or cur_s<=new_s<=cur_e or cur_s<=new_e<=cur_e 
        
        
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        l,n = 0,len(intervals)
        
        while l < n and not self.is_overlapping(intervals,l,newInterval):
            # check if it is current place for new interval
            if newInterval.end<intervals[l].start:
                intervals.insert(l,newInterval)
                return intervals
            l += 1
        
        if l == n:
            intervals.append(newInterval)
            return intervals
        
        r = l+1
        while r < n and self.is_overlapping(intervals,r,newInterval):
            r += 1
        r -= 1
        
        new_s = min(newInterval.start,intervals[l].start)
        new_e = max(newInterval.end,intervals[r].end)
        
        intervals = intervals[:l]+[Interval(new_s,new_e)] + intervals[r+1:]
        return intervals
        