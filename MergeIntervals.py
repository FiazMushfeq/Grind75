from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    return None

intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
print(merge(intervals))

intervals = [[1,4],[4,5]]
# Output: [[1,5]]
print(merge(intervals))