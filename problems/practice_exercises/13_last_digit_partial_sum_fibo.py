# -----------------------
def fibo_num_naive(n):
    """
    There's no need in saving all the numbers from fibonacci if we're
    only interest in the last digit.
    """
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


def last_digit_partial_sum_fibo_naive(m, n):
    current = fibo_num_naive(m)
    previous = fibo_num_naive(m - 1)
    fibo_sum = current
    for _ in range(m, n):
        previous, current = current, previous + current
        fibo_sum += current
    return fibo_sum % 10
# -----------------------

def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m

        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1

def fib_last_digit(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current

def last_digit_partial_sum_fibo(m, n):
    if n <= 0:
        return 0

    # Find Pisano period for modulo 10
    pisano_period_10 = pisano_period(10)

    # Reduce m and n modulo the Pisano period
    m %= pisano_period_10
    n %= pisano_period_10

    # Ensure m is less than or equal to n
    if m > n:
        m, n = n, m

    # Compute the last digit of Fibonacci sum from m to n
    sum_last_digit = 0
    for i in range(m, n + 1):
        sum_last_digit = (sum_last_digit + fib_last_digit(i)) % 10

    return sum_last_digit

if __name__ == "__main__":
    lst = [(0, 0), (0, 1), (0, 7), (3, 7), (10, 10), (1, 100000000)]
    for m, n in lst:
        print(f"m = {m}, n = {n} --> last digit = {last_digit_partial_sum_fibo(m, n)}")
