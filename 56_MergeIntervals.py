# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return intervals
        
        intervals = sorted(intervals)
        res = []
        start_idx, end_idx = 0, 0
        for i in range(len(intervals)-1):
            if intervals[i].end < intervals[i+1].start:
                res.append([intervals[start_idx].start, intervals[end_idx].end])
                start_idx = i+1
                end_idx = i+1
            else:
                end_idx = i+1
            print(start_idx, end_idx)
        print(start_idx, end_idx)
        print(intervals[0].start, intervals[0].end)
        if len(intervals) >= 2:
            print(intervals[1].start, intervals[1].end)
#        print(intervals[start_idx].start, intervals[end_idx].end)
        res.append([intervals[start_idx].start, intervals[end_idx].end])
        return res
