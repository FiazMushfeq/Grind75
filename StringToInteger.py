import math
import re

def myAtoi(s: str) -> int:
    # Remove whitespaces
    s = s.strip()
    if len(s) == 0:
        return 0
    # Check for negative sign and remove from s
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    # Read in numberical value
    match = re.search(r"^[\d]+", s)
    if not match:
        return 0
    s = match.group(0)
    # Return s after converting and applying sign, check size
    s = int(s) * sign
    if s < math.pow(-2, 31):
        return int(math.pow(-2, 31))
    elif s > (math.pow(2, 31) - 1):
        return int(math.pow(2, 31) - 1)
    else:
        return s

# Test cases
print(myAtoi("42"))  # Output: 42
print(myAtoi("   -42"))  # Output: -42
print(myAtoi("4193 with words"))  # Output: 4193
print(myAtoi("words and 987"))  # Output: 0
print(myAtoi("-91283472332"))  # Output: -2147483648