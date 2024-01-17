from typing import List

def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(nlogn) sort the list
        # nums = nums.sort()

nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
sortColors(nums)
print(nums)

nums = [2,0,1]
# Output: [0,1,2]
sortColors(nums)
print(nums)