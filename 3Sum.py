from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # Brute force: O(n^3)
    # results = []
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         for k in range(j + 1, len(nums)):
    #             if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
    #                 sortedTriplet = sorted([nums[i], nums[j], nums[k]])
    #                 if sortedTriplet not in results:
    #                     results.append(sortedTriplet)
    # return results

    # Loop through list once, then use TwoSumII approach: O(n^2)
    results = []
    nums = sorted(nums) # O(nlogn)
    # numsDict = dict()
    for index, target in enumerate(nums):
        # x + y + z = 0
        left, right = index + 1, len(nums) - 1
        while left < right:
            currSum = target + nums[left] + nums[right]
            if currSum == 0:
                # Solution found!
                # print([index, left, right])
                results.append([target, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            elif currSum < 0:
                left += 1
            else:
                right -= 1
    return results

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(threeSum(nums))

nums = [0,1,1]
# Output: []
print(threeSum(nums))

nums = [0,0,0]
# Output: [[0,0,0]]
print(threeSum(nums))

nums = [0,0,0,0]
# Output: [[0,0,0]]
print(threeSum(nums))