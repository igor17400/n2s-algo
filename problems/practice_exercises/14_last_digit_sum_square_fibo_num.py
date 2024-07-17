# -------------------------
def last_digit_sum_square_fibo_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    fibo_sum = current
    for _ in range(n - 1):
        previous, current = current, previous + current
        fibo_sum += current * current
    return fibo_sum % 10
# -------------------------

def pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1
    return 0

def last_digit_sum_square_fibo(n):
    if n <= 1:
        return n

    pisano_period_10 = pisano_period(10)
    n_mod_period = n % pisano_period_10

    previous = 0
    current = 1
    fibo_sum_square_last_digit = 1  # Start with 1 because F(1)^2 = 1

    for _ in range(2, n_mod_period + 1):
        previous, current = current, (previous + current) % 10
        fibo_sum_square_last_digit = (fibo_sum_square_last_digit + (current * current) % 10) % 10

    return fibo_sum_square_last_digit

if __name__ == "__main__":
    lst = [7, 73, 78134, 832564823476]
    for n in lst:
        print(f" n = {n} --> last digit sum squares = {last_digit_sum_square_fibo(n)}")
