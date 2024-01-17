from collections import Counter
from typing import List

def majorityElement(nums: List[int]) -> int:
    # O(n) time complexity and O(n) space complexity
    # count = Counter(nums)
    # return (count.most_common(1)[0][0])

    # Moore's Voting Algorithm: O(n) time complexity and O(1) space complexity
    elem = None
    count = 0
    for x in nums:
        if count == 0:
            elem = x
        if x == elem:
            count += 1
        else:
            count -= 1
    return elem

nums = [3,2,3]
# Output: 3
print(majorityElement(nums))

nums = [2,2,1,1,1,2,2]
# Output: 2
print(majorityElement(nums))