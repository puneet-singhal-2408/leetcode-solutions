"""
Leetcode Problem No 88: Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?
"""


def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # remove the 0 from list 1 representing number of elements in list 2
    # for each element in list 2 compare it with each element of list1
    # if value in list 2 is less than equal to value in list 1
    # put the value in list2 at place of value in list1
    # move to next value in  list 2
    while n != 0:
        nums1.pop()
        n -= 1
    for value2 in nums2:
        next_v = False
        for value1 in nums1:
            if value2 <= value1:
                nums1.insert(nums1.index(value1), value2)
                next_v = True
                break
        if not next_v:
            nums1.append(value2)

    return nums1


# sample test cases:
print(merge([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3))
print(merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3))
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
print(merge([2, 0], 1, [1], 1))
print(merge([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5))
print(merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5))
print(merge([-1, 0, 1, 1, 0, 0, 0, 0, 0], 4, [-1, 0, 2, 2, 3], 5))
