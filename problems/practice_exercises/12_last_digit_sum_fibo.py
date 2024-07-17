def last_digit_sum_fibo_naive(n):
    """
    There's no need in saving all the numbers from fibonacci if we're
    only interest in the last digit.
    """
    if n <= 1:
        return n
    previous = 0
    current = 1
    fibo_sum = current
    for _ in range(n - 1):
        previous, current = current, previous + current
        fibo_sum += current
    return fibo_sum % 10


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def last_digit_sum_fibo(n):
    if n <= 1:
        return n

    # Calculate Pisano period for modulo 10
    pisano_mod_10 = pisano_period(10)
    n_mod_pisano = n % pisano_mod_10
    
    previous = 0
    current = 1
    fibo_sum = current
    
    for _ in range(1, n_mod_pisano):
        previous, current = current, (previous + current) % 10
        fibo_sum = (fibo_sum + current) % 10
    
    return fibo_sum


if __name__ == "__main__":
    lst = [3, 100, 613455, 832564823476]
    for n in lst:
        print(f"n = {n} --> last digit = {last_digit_sum_fibo(n)}")
