def max_consecutive_ones(lst):
    max_count = 0
    count = 0
    for element in lst:
        if element == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count


print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(max_consecutive_ones([1, 0, 1, 1, 0, 1]))
