"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0,
which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


def jump_game(nums):
    max_jump = 0
    for i, jump in enumerate(nums):
        if i > max_jump:
            return False
        max_jump = max(max_jump, i + jump)
    return True


print(jump_game([3, 0, 8, 2, 0, 0, 1]))
print(jump_game([0]))
print(jump_game([0, 1]))
print(jump_game([2, 0]))
print(jump_game([2, 0, 0]))
print(jump_game([2, 3, 1, 1, 4]))
print(jump_game([3, 2, 1, 0, 4]))
print(jump_game([3, 2, 2, 0, 1, 4]))
