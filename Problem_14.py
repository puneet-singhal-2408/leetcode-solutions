"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longest_common_prefix(strs):
    if not strs:
        return ""
    # get the length of smallest string.
    min_len = min(len(s) for s in strs)
    # the possible longest common prefix will be
    prefix = strs[0][:min_len]
    for s in strs:
        # now check how much part of prefix is common in strings
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["flower", "dlow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
