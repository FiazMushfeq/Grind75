from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    # Using dictionary
    dictS = dict(Counter(s))
    for c in t:
        if c not in dictS:
            return False
        dictS[c] -= 1
        if dictS[c] == 0:
            del dictS[c]
    return not bool(dictS)

s = "anagram"
t = "nagaram"
# Output: true
print(isAnagram(s, t))

s = "rat"
t = "car"
# Output: false
print(isAnagram(s, t))