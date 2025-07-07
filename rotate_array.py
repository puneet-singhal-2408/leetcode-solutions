"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""


def rotate_array(nums, k):
    while k != 0:
        nums.insert(0, nums[-1])
        nums.pop(-1)
        k -= 1
    return nums

# without using in built functions
def rotate(nums, k):
    # Get the actual number of rotations
    k = k % len(nums)
    # Get the number of elements to move from the end to the beginning
    r = len(nums) - k
    # Store the elements to move
    new = nums[0:r]
    # Remove the elements from the beginning
    nums[0:r] = []
    # Append the stored elements to the end
    nums.extend(new)
    return nums


print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate_array([-1, -100, 3, 99], 2))
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(rotate([-1, -100, 3, 99], 2))
