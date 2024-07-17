def naive_fibonacci_number(n):
    if n == 0 or n == 1:
        return n
    return naive_fibonacci_number(n - 2) + naive_fibonacci_number(n - 1)



memo = {}
def fibonacci_number(n):
    """
    Optimization using memoization approach
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_number(n - 2) + fibonacci_number(n - 1)
    return memo[n]

if __name__ == "__main__":
    for i in range(11):
        print(f"n = {i} -> {naive_fibonacci_number(n = i)}") 
    for i in range(11):
        print(f"n = {i} -> {fibonacci_number(n = i)}") 