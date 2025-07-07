"""

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

"""


# using counting sort

def sort_colors(nums):
    count0 = count1 = count2 = 0

    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1
    nums[:count0] = [0] * count0
    nums[count0: count0 + count1] = [1] * count1
    nums[count0 + count1:] = [2] * count2
    return nums


# sort colors using three pointer
def sort_colors_three_pointers(nums):
    count0 = count1 = 0
    count2 = len(nums) - 1

    while count1 <= count2:
        if nums[count1] == 0:
            nums[count1], nums[count0] = nums[count0], nums[count1]
            count0 += 1
            count1 += 1
        elif nums[count1] == 1:
            count1 += 1
        else:
            nums[count1], nums[count2] = nums[count2], nums[count1]
            count2 -= 1
    return nums


print(sort_colors_three_pointers([2, 0, 2, 1, 1, 0]))
print(sort_colors_three_pointers([2, 0, 1]))
print(sort_colors_three_pointers([1, 0, 2]))
print(sort_colors_three_pointers([0, 1, 2]))
print(sort_colors_three_pointers([2, 1, 0]))
print(sort_colors_three_pointers([1, 2, 0]))
