from typing import Counter

def lengthOfLongestSubstring(s: str) -> int:
    # Brute Force: O(n^2)
    # longestLength = 0
    # if len(s) == 1:
    #     return 1
    # for x in range(len(s)):
    #     for y in range(x + 1, len(s) + 1, 1):
    #         t = s[x:y]
    #         # print(t)
    #         if len(t) == len(Counter(t)):
    #             if len(t) > longestLength:
    #                 longestLength = len(t)

    # Sliding Window with Set: O(n)
    longestLength = 0
    unique = set()
    left, right = 0, 0
    while right < len(s):
        if s[right] not in unique:
            unique.add(s[right])
            longestLength = max(longestLength, right - left + 1)
            right += 1
        else:
            unique.remove(s[left])
            left += 1
    return longestLength

s = "abcabcbb"
# Output: 3
print(lengthOfLongestSubstring(s))

s = "bbbbb"
# Output: 1
print(lengthOfLongestSubstring(s))

s = "pwwkew"
# Output: 3
print(lengthOfLongestSubstring(s))

s = "aab"
# Output: 2
print(lengthOfLongestSubstring(s))