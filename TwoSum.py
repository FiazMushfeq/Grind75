from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # O(n^2): basic solution by iterating
    # for index1, value1 in enumerate(nums):
    #     for index2, value2 in enumerate(nums):
    #         if index1 != index2 and value1 + value2 == target:
    #             return [index1, index2]

    # O(nlogn): sorting the list first then using two pointers
    # sortedNums = sorted(nums)
    # ptr1, ptr2 = 0, len(nums) - 1
    # while ptr1 < ptr2:
    #     if sortedNums[ptr1] + sortedNums[ptr2] == target:
    #         if sortedNums[ptr1] == sortedNums[ptr2]:
    #             return [nums.index(sortedNums[ptr1]), nums.index(sortedNums[ptr2], 1)]
    #         return [nums.index(sortedNums[ptr1]), nums.index(sortedNums[ptr2])]
    #     if sortedNums[ptr1] + sortedNums[ptr2] > target:
    #         ptr2 -= 1
    #     if sortedNums[ptr1] + sortedNums[ptr2] < target:
    #         ptr1 += 1

    # O(n): using hashmap / dictionary
    numsDict = dict()
    for index, value in enumerate(nums):
        if target - value in numsDict:
            return [numsDict[target - value], index]
        numsDict[value] = index

# nums = [2,7,11,15], target = 9
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
# nums = [3,2,4], target = 6
nums = [3,2,4]
target = 6
print(twoSum(nums, target))
# nums = [3,3], target = 6
nums = [3,3]
target = 6
print(twoSum(nums, target))