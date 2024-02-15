from collections import Counter

def longestPalindrome(s: str) -> int:
    dictS = dict(Counter(s))
    # print(dictS)
    length = 0
    hasOdd = False
    for value in dictS.values():
        if value % 2 == 0:
            length += value
        else:
            hasOdd = True
            length += value - 1
    if hasOdd:
        length += 1
    return length

s = "abccccdd"
# Output: 7
print(longestPalindrome(s))

s = "a"
# Output: 1
print(longestPalindrome(s))

s = "Aa"
# Output: 7
print(longestPalindrome(s))