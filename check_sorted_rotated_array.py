def is_sorted_rotated(nums):
    if len(nums) <= 1:
        return True
    sorted_nums = sorted(nums)
    for _ in nums:
        nums = nums[-1:] + nums[:-1]
        if sorted_nums == nums:
            return True
    return False


print(is_sorted_rotated([3, 4, 5, -1, 2]))
print(is_sorted_rotated([1, 2, 3]))
print(is_sorted_rotated([2, 1, -3, 4]))
print(is_sorted_rotated([2]))
print(is_sorted_rotated([]))
