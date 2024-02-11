from typing import List

def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(nlogn) sort the list
        # nums = nums.sort()

        # O(n): counting sort / quick sort
        zero, one, two = 0, 0, len(nums) - 1
        while one <= two:
                if nums[one] == 1:
                        one += 1
                elif nums[one] == 2:
                        nums[one], nums[two] = nums[two], nums[one]
                        two -= 1
                else:
                        nums[zero], nums[one] = nums[one], nums[zero]
                        zero += 1
                        one += 1

nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
sortColors(nums)
print(nums)

nums = [2,0,1]
# Output: [0,1,2]
sortColors(nums)
print(nums)