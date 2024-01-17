from re import sub

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = sub(r"[^a-zA-Z0-9]", "", s)
    return s == s[::-1]

s = "A man, a plan, a canal: Panama"
# Output: true
print(isPalindrome(s))

s = "race a car"
# Output: false
print(isPalindrome(s))

s = " "
# Output: true
print(isPalindrome(s))