def gcd_naive(a, b):
    """
    To simplify our problem, we focus solely on the smaller element 
    between a and b. This approach works because the greatest common 
    divisor of a and b is never greater than either a or b.
    """
    _min = min(a, b)
    _max = max(a, b)
    _max_div = 0
    for divisor in range(1, _min + 1):
        if _min % divisor == 0 and _max % divisor == 0:
            _max_div = max(divisor, _max_div)
    return _max_div

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    lst = [(100, 30), (28851538, 1183019)]
    for a, b in lst:
        print(f" a = {a}, b = {b} --> gcd = {gcd(a, b)}")
