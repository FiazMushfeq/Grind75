from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    if not (s and t):
        return ""
    dictT = dict(Counter(t))
    dictCurr = defaultdict(int)
    # print("dictT: " + str(dictT))
    # print("dictCurr: " + str(dictCurr))
    left = 0
    have = 0
    min_start, min_length = 0, len(s) + 1
    # Iterate right pointer to find substring
    for right, value in enumerate(s):
        dictCurr[value] += 1
        if value in dictT and dictT[value] >= dictCurr[value]:
            have += 1
        # print("Check current window: " + str(dictCurr))
        # Window holds t and attempt to increment left
        # Check if current window has at least the freq of the value in dictT/freq of T
        while have == len(t) and left <= right:
            # print("Check current valid window: " + str(dictCurr))
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length
                min_start = left
            # Since we're about move up left, decrement frequency of left
            dictCurr[s[left]] -= 1
            if dictCurr[s[left]] == 0:
                del dictCurr[s[left]]
            if s[left] in dictT and dictCurr[s[left]] < dictT[s[left]]:
                have -= 1
            left += 1
    # print(str(left) + ", " + str(right))
    if min_length == len(s) + 1:
        return ""
    return s[min_start : min_start + min_length]

s, t = "ADOBECODEBANC", "ABC"
# Output: "BANC"
print(minWindow(s, t))

s, t = "a", "a"
# Output: "a"
print(minWindow(s, t))

s, t =  "a", "aa"
# Output: ""
print(minWindow(s, t))

s, t =  "aa", "aa"
# Output: "aa"
print(minWindow(s, t))