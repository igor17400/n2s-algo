import math as m

def lcm_naive(a, b):
    _min_div = m.inf
    for _num in range(1, a * b + 1):
        if _num % a == 0 and _num % b == 0:
            _min_div = min(_num, _min_div)
            if _min_div == _num:
                break
    return _min_div

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    # lst = [(2, 3), (9, 13)]
    # for a, b in lst:
    #     print(f" a = {a}, b = {b} --> lcm = {lcm(a, b)}")
    a, b = map(int, input().split())
    print(lcm(a, b))
