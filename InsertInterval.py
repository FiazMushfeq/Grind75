from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    # for x in range(len(intervals)):
    #     # newInterval does not overlap
    #     if newInterval[0] > intervals[x][1]:
    #         result.append(intervals[x])
    #     # insert newInterval and return rest of intervals
    #     elif newInterval[1] < intervals[x][0]:
    #         result.append(newInterval)
    #         return result + intervals[x:]
    #     # newInterval overlaps
    #     else:
    #         newInterval = [min(intervals[x][0], newInterval[0]), max(intervals[x][1], newInterval[1])]
    # result.append(newInterval)

    i = 0
    # Append intervals to result before newInterval is inserted
    while i < len(intervals) and newInterval[0] > intervals[i][1]:
        result.append(intervals[i])
        i += 1
    # Insert newInterval when overlapping
    while i < len(intervals) and newInterval[1] >= intervals[i][0]:
        newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        i += 1
    # Merge new interval
    result.append(newInterval)
    # Add remaining intervals and return result
    return result + intervals[i:]

intervals, newInterval = [[1,3],[6,9]], [2,5]
# Output: [[1,5],[6,9]]
print(insert(intervals, newInterval))

intervals, newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
# Output: [[1,2],[3,10],[12,16]]
print(insert(intervals, newInterval))