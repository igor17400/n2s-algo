def max_inner_product(a, b):
    # Sort both vectors in descending order
    a.sort(reverse=True)
    b.sort(reverse=True)
    
    # Compute the dot product of the sorted vectors
    max_product = sum(x * y for x, y in zip(a, b))
    
    return max_product

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_inner_product(prices, clicks))
