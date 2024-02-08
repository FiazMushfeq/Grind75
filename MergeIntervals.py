from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Sort intervals by first indexes
    intervals.sort(key=lambda x: x[0])
    # print(intervals)
    # Loop through intervals and merge
    result = [intervals[0]]
    for x in intervals[1:]:
        # print(x)
        # Check for overlap
        if result[-1][1] >= x[0]:
            # Merge
            result[-1] = [result[-1][0], max(result[-1][1], x[1])]
        # No overlap
        else:
            result.append(x)
    return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
print(merge(intervals))

intervals = [[1,4],[4,5]]
# Output: [[1,5]]
print(merge(intervals))

intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
print(merge(intervals))