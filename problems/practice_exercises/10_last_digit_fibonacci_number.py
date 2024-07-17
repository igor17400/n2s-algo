def last_digit_fibo_naive(n):
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
    return current % 10

def last_digit_fibo(n):
    """
    Calculate the last digit of the nth Fibonacci number.
    """
    if n <= 1:
        return n
    
    previous_last_digit = 0
    current_last_digit = 1
    
    for _ in range(2, n + 1):
        next_last_digit = (previous_last_digit + current_last_digit) % 10
        previous_last_digit = current_last_digit
        current_last_digit = next_last_digit
    
    return current_last_digit


if __name__ == "__main__":
    n_lst = [3, 139, 91239]
    for n in n_lst:
        print(f"n = {n} --> last digit = {last_digit_fibo(n = n)}")
