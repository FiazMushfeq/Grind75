from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    # O(n) time, O(n) space: convert to dictionary / hashmap
    # numbersDict = dict()
    # for index, value in enumerate(numbers):
    #     index += 1
    #     if target - value in numbersDict:
    #         return [index, numbersDict[target - value]] if index < numbersDict[target - value] else [numbersDict[target - value], index]
    #     numbersDict[value] = index

    # O(n) time, O(1) space: search with two points, like BS
    left, right = 0, len(numbers) - 1
    while left < right:
        currSum = numbers[left] + numbers[right]
        if currSum == target:
            return left + 1, right + 1
        elif currSum < target:
            left += 1
        else:
            right -= 1
    return None

# Your solution must use only constant extra space.

numbers, target = [2,7,11,15], 9
# Output: [1,2]
print(twoSum(numbers, target))

numbers, target = [2,3,4], 6
# Output: [1,3]
print(twoSum(numbers, target))

numbers, target = [-1,0], -1
# Output: [1,2]
print(twoSum(numbers, target))