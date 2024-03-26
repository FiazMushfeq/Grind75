from typing import List

# 54. Spiral Matrix
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    # print(m)
    # print(n)
    return None

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
print(spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiralOrder(matrix))