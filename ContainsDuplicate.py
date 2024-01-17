from collections import defaultdict
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    numsDict = {}
    for x in nums:
        if x in numsDict:
            return True
        numsDict[x] = 0
    return False

nums = [1,2,3,1] 
# output: True
print(containsDuplicate(nums))

nums = [1,2,3,4] 
# output: False
print(containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2] 
# output: True
print(containsDuplicate(nums))