def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]


print(fibonacci_memo(2))
print(fibonacci_memo(5))
print(fibonacci_memo(15))
