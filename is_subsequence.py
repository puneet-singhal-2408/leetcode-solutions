"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining
characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

"""


def is_subsequence(s, t):
    if len(s) == 0:
        return True
    l, r = 0, 0
    while l <= len(s)-1 and r <= len(t) - 1:
        if s[l] == t[r]:
            l += 1
            r += 1
        else:
            r += 1
    if l != len(s):
        return False
    else:
        return True


print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
print(is_subsequence("acb", "ahbgdc"))
print(is_subsequence("b", "c"))
print(is_subsequence("aaaaaa", "bbaaaa"))
