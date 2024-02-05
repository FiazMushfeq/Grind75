from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    return None

candidates, target = [2,3,6,7], 7
# Output: [[2,2,3],[7]]
print(combinationSum(candidates, target))

candidates, target = [2,3,5], 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
print(combinationSum(candidates, target))

candidates, target = [2], 1
# Output: []
print(combinationSum(candidates, target))