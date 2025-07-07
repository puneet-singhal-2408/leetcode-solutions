def find_unique_element(lst):
    xor_0 = 0
    for num in lst:
        xor_0 ^= num
    return xor_0


print(find_unique_element([4, 1, 2, 1, 2]))
