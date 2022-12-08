LeetCode 56 - Merge Intervals [medium]

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
Explanation: Since intervals [1, 3] and [2, 6] overlaps, merge them into [1, 6].

CODE

class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:  # overlapping intervals
                end = max(interval[1], end)
            else:  # non-overlapping interval, add the previous interval and reset
                merged.append([start, end])
                start = interval[0]
                end = interval[1]
            
        merged.append([start, end])  # add the last interval
        return merged