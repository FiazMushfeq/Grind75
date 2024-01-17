from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    left, right = [], []
    for curr in intervals:
        # current interval is greater than newInterval
        if newInterval[0] > curr[1]:
            left.append(curr)
        # current interval is less than newInterval
        elif newInterval[1] < curr[0]:
            right.append(curr)
        # merge newInterval with current interval
        else:
            newInterval = [min(newInterval[0], curr[0]), max(newInterval[1], curr[1])]
    return left + right

intervals, newInterval = [[1,3],[6,9]], [2,5]
# Output: [[1,5],[6,9]]
print(insert(intervals, newInterval))

intervals, newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
# Output: [[1,2],[3,10],[12,16]]
print(insert(intervals, newInterval))