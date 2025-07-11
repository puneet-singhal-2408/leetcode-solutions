"""
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

Example 1:
Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

Example 2:
Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
"""


def happy_prefix(s):
    prefix = ""
    l, r = 1, -1

    while l < len(s):
        if s[:l] == s[r:]:
            if len(prefix) < len(s[:l]):
                prefix = s[:l]
        l += 1
        r -= 1
    return prefix


print(happy_prefix("level"))
print(happy_prefix("ababab"))
