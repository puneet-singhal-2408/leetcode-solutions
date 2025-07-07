def number_of_points(nums):
    points = [i for start, end in nums for i in range(start, end + 1)]
    return len(set(points))


def number_of_points_line(nums):
    points = set()
    for start, end in nums:
        points.update(range(start, end + 1))
    return len(points)


print(number_of_points([[3, 6], [1, 5], [4, 7]]))
print(number_of_points([[1, 3], [5, 8]]))
