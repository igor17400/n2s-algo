def money_change_naive(n: int, d: dict):
    if n == 0:
        return n
    elif n < 5:
        d['1'] += 1
        return money_change_naive(n - 1, d)
    elif n < 10:
        d['5'] += 1
        return money_change_naive(n - 5, d)
    else:
        d['10'] += 1
        return money_change_naive(n - 10, d)

if __name__ == '__main__':
    lst = [2, 28]
    for n in lst:
        d = {'1': 0, '5': 0, '10': 0}
        money_change_naive(n, d)
        print(d)