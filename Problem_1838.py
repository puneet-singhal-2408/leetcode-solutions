def max_frequency(nums, k):
    nums.sort()
    left = 0
    total = 0
    max_freq = 0

    for right in range(len(nums)):
        total += nums[right]

        while nums[right] * (right - left + 1) > total + k:
            total -= nums[left]
            left += 1

        max_freq = max(max_freq, right - left + 1)

    return max_freq


# Example usage:
nums = [1, 2, 4]
k = 5
print(max_frequency(nums, k))  # Output: 3

nums = [1, 4, 8, 13]
k = 5
print(max_frequency(nums, k))  # Output: 2
