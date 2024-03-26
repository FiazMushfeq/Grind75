from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(floodFill(image, sr, sc, color))
# Output: [[2,2,2],[2,2,0],[2,0,1]]

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
print(floodFill(image, sr, sc, color))
# Output: [[0,0,0],[0,0,0]]