from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    results = []
    def backtrack(index, path, target, results):
        # If target is negative, path is too large
        if target < 0:
            return
        # When target is 0, add current path
        if target == 0:
            # Clone path since solution is found
            results.append(path[:])
            return
        # Compute candidates for target
        for x in range(index, len(candidates)):
            path.append(candidates[x])
            backtrack(x, path, target - candidates[x], results)
            path.pop()
    backtrack(0, [], target, results)
    return results

candidates, target = [2,3,6,7], 7
# Output: [[2,2,3],[7]]
print(combinationSum(candidates, target))

candidates, target = [2,3,5], 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
print(combinationSum(candidates, target))

candidates, target = [2], 1
# Output: []
print(combinationSum(candidates, target))