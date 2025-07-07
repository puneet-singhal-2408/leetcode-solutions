"""
Given an integer array nums,
move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


def move_zeros(lst):
    j = -1
    # get index of first zero in given array
    # we can use in-built function index() to get index of zero but if no zeros are present in array it will give error.
    for i in range(0, len(lst)):
        if lst[i] == 0:
            j = i
            break
    if j == -1:
        return lst

    for i in range(j+1, len(lst)):
        if lst[i] != 0:
            lst[i], lst[j] = lst[j], lst[i]
            j += 1
    return lst



print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([0]))
