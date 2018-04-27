# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 15:53:50 2018

@author: I309535
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def is_overlapping(self,cur_s,cur_e,newInterval):
        new_s = newInterval.start
        new_e = newInterval.end
        return new_s<=cur_s<=new_e or new_s<=cur_e<=new_e or cur_s<=new_s<=cur_e or cur_s<=new_e<=cur_e 
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        l,n = 0,len(intervals)
        if n < 2:
            return intervals
        
        intervals.sort(key=lambda x:(x.start,x.end))
        result = []
        
        while l < n:
            new_s = intervals[l].start
            new_e = intervals[l].end
            r = l+1
            
            while r < n and self.is_overlapping(new_s,new_e,intervals[r]):
                new_s = min(new_s,intervals[r].start)
                new_e = max(new_e,intervals[r].end)
                r += 1
                
            interval = Interval(new_s,new_e)
            result.append(interval)
            l = r
            
        return result
                
                
            