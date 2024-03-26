from typing import List

def moveZeroes(nums: List[int]):
        result = []
        for x in nums:
            if x != 0:
                result.append(x)
        nums = result + [0] * (len(nums) - len(result))
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """

nums = [0,1,0,3,12]
print(moveZeroes(nums))
# print(nums)
# Output: [1,3,12,0,0]

nums = [0]
print(moveZeroes(nums))
# print(nums)
# Output: [0]