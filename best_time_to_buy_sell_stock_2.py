def max_profit_made(prices):
    max_profit = [0]
    n = len(prices)
    left, right = 0, 1
    while right < n:
        if prices[right] > prices[left]:
            max_profit.append(prices[right] - prices[left])
        left += 1
        right += 1
    return sum(max_profit)


print(max_profit_made([7, 1, 5, 3, 6, 4]))
print(max_profit_made([1, 2, 3, 4, 5]))
print(max_profit_made([7, 6, 4, 3, 1]))
