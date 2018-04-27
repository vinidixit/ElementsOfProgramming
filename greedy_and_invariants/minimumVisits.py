# -*- coding: utf-8 -*-
"""
Created on Sun Apr 08 15:52:43 2018

@author: I309535
"""
## ********* find minimum cover

def findMinimumVisits(intervals):
    # sort in order of end times
    intervals.sort(key=lambda x:x[1])
    minimum_visits = list()
    i,n = 0,len(intervals)
    
    while i < n:
        cur_time = intervals[i][1]
        minimum_visits.append(cur_time)
        j = i+1
        while j < n:
            if cur_time in intervals[j]:
                j+=1
            else:
                break
        
        i = j
        
    return minimum_visits
        

intervals = [[1,2],[2,3],[3,4],[2,3],[3,4],[4,5]]#[[0,3],[2,6],[3,4],[6,9]]
print findMinimumVisits(intervals)