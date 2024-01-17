from collections import Counter

def longestPalindrome(s: str) -> int:
    dictS = dict(Counter(s))
    for c in t:
        if c not in dictS:
            return False
        dictS[c] -= 1
        if dictS[c] == 0:
            del dictS[c]
    return 0

s = "abccccdd"
# Output: 7
print(longestPalindrome(s))

s = "a"
# Output: 1
print(longestPalindrome(s))