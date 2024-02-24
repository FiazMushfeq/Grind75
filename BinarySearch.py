from typing import List

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

nums, target = [-1,0,3,5,9,12], 9
# Output: 4
print(search(nums, target))

nums, target = [-1,0,3,5,9,12], 2
# Output: -1
print(search(nums, target))