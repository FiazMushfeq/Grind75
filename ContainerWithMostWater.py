from typing import List

def maxArea(height: List[int]) -> int:
    # Initial start, end, and area
    start, end = 0, len(height) - 1
    area = min(height[start], height[end]) * (end - start)
    while start < end:
        if height[start] <= height[end]:
            start += 1
        else:
            end -= 1
        tempArea = min(height[start], height[end]) * (end - start)
        if tempArea > area:
            area = tempArea
    return area

height = [1,8,6,2,5,4,8,3,7]
# Output: 49
print(maxArea(height))

height = [1,1]
# Output: 1
print(maxArea(height))

height = [2,3,4,5,18,17,6]
# Output: 17
print(maxArea(height))