from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    # write an algorithm that runs in O(n) time and without using the division operation

    # O(n^2): brute force with nested loops
    # result = []
    # for x in nums:
    #     product = 1
    #     copyNums = nums.copy()
    #     copyNums.remove(x)
    #     for y in copyNums:
    #         product *= y
    #     result.append(product)
    # return result

    # O(n) time and space complexity: compute prefix and suffix products
    # result = []
    # leftProd = [1] * len(nums)
    # rightProd = [1] * len(nums)
    # for x in range(1, len(nums)):
    #     leftProd[x] = leftProd[x - 1] * nums[x - 1]
    #     rightProd[len(nums) - x - 1] = rightProd[len(nums) - x] * nums[len(nums) - x]
    # for x in range(len(nums)):
    #     result.append(leftProd[x] * rightProd[x])
    # return result

    # O(n) time and O(1) space complexity: using prefix / postfix and saving it in result array, which doesn't count for linear space
    result = [1] * len(nums)
    prefix = 1
    for x in range(len(nums)):
        result[x] *= prefix
        prefix *= nums[x]
    postfix = 1
    for x in range(len(nums) - 1, -1, -1):
        result[x] *= postfix
        postfix *= nums[x]
    return result

nums = [1,2,3,4]
# Output: [24,12,8,6]
print(productExceptSelf(nums))

nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
print(productExceptSelf(nums))