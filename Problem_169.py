"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""


def majority_element(nums):
    majority = len(nums) // 2 + 1
    nums.sort()
    return nums[majority - 1]


def majority_element2(nums):
    count = 0
    candidate = nums[0]
    for num in nums:
        if num == candidate:
            count += 1


print(majority_element([3]))
print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
