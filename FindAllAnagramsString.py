from collections import Counter, defaultdict
from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    result = []
    # p is > than s
    if len(p) > len(s):
        return result
    # Brute Force
    # dictP = dict(Counter(p))
    # # print(dictP)
    # for x in range(len(s) - len(p) + 1):
    #     if dictP == dict(Counter(s[x : x + len(p)])):
    #         result.append(x)

    # Sliding Window Technique
    dictCurr = defaultdict(int)
    # for x in p:
    #     result[x] += 1
    dictP = dict(Counter(p))
    left, right = 0, 0
    while right < len(s):
        dictCurr[s[right]] += 1
        # Current window is too big
        if right - left + 1 > len(p):
            # Since we're about move up left, decrement frequency of left
            dictCurr[s[left]] -= 1
            if dictCurr[s[left]] == 0:
                del dictCurr[s[left]]
            # Move left pointer up by one
            left += 1
        # Found anagram of pattern
        if right - left + 1 == len(p):
            if dictP == dictCurr:
                result.append(left)
        right += 1
    return result

s, p = "cbaebabacd", "abc"
# Output: [0,6]
print(findAnagrams(s, p))

s, p = "abab", "ab"
# Output: [0,1,2]
print(findAnagrams(s, p))