def longestPalindrome(s: str) -> str:
    # Only looks for middle palindrome: WRONG
    # # print("Starting...")
    # while not checkPalindrome(s):
    #     # Remove first element
    #     if checkPalindrome(s[1:]):
    #         s = s[1:]
    #     # Remove last element
    #     elif checkPalindrome(s[:-1]):
    #         s = s[:-1]
    #     # Remove first and last elements
    #     else:
    #         s = s[1:-1]
    # # print("Returning...")
    
    # Center around approach : O(n^2)
    if len(s) < 2:
        return s
    longestPal = s[0]

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
    
    for x in range(len(s) - 1):
        odd = expand(x, x)
        even = expand(x, x + 1)
        if len(odd) > len(longestPal):
            longestPal = odd
        if len(even) > len(longestPal):
            longestPal = even

    return longestPal

# def checkPalindrome(s: str) -> bool:
#     return s == s[::-1]

s = "babad"
# Output: "bab"
print(longestPalindrome(s))

s = "cbbd"
# Output: "bb"
print(longestPalindrome(s))

s = "ca"
# Output: "a"
print(longestPalindrome(s))

s = "eabcb"
# Output: "bcb"
print(longestPalindrome(s))

s = "bb"
# Output: "bb"
print(longestPalindrome(s))