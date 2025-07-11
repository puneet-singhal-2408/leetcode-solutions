"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number in the range since it does not appear in nums.
"""


def missing_number(arr):
    # find the sum of n natural numbers
    n = len(arr)
    sum_of_n = (n * (n + 1)) // 2
    sum_of_arr = sum(arr)
    return sum_of_n - sum_of_arr


def missing_number_cyclic_sort(nums):
    n = len(nums)
    i = 0
    while i < n:
        correct = nums[i]
        if correct < n and correct != nums[correct]:
            nums[correct], nums[i] = nums[i], nums[correct]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i:
            return i
    return n


# implement using XOR

print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missing_number_cyclic_sort([3, 0, 1]))
print(missing_number_cyclic_sort([0, 1]))
print(missing_number_cyclic_sort([9, 6, 4, 2, 3, 5, 7, 0, 1]))
