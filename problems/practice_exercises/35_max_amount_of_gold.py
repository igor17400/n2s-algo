from sys import stdin


def maximum_gold(capacity, weights):
    n = len(weights)
    # Create a DP table with dimensions (n+1) x (capacity+1) initialized to 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight is less than or equal to the current capacity
            if weights[i - 1] <= w:
                # Choose the maximum of including or excluding the current item
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + weights[i - 1]
                )
            else:
                # If the current item is too heavy, exclude it
                dp[i][w] = dp[i - 1][w]

    # The maximum amount of gold is stored in the bottom-right cell of the DP table
    return dp[n][capacity]


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (10, [1, 4, 8]),  # Capacity: 10, Weights: [1, 4, 8]
        (20, [5, 7, 12, 18]),  # Capacity: 20, Weights: [5, 7, 12, 18]
        (15, [2, 3, 4, 5, 6]),  # Capacity: 15, Weights: [2, 3, 4, 5, 6]
        (5, [1, 2, 3, 4, 5]),  # Capacity: 5, Weights: [1, 2, 3, 4, 5]
        (0, [1, 2, 3]),  # Edge case: Capacity 0
        (100, []),  # Edge case: No weights
    ]

    for i, (capacity, weights) in enumerate(test_cases, 1):
        result = maximum_gold(capacity, weights)
        print(f"Test case {i}:")
        print(f"  Capacity: {capacity}")
        print(f"  Weights: {weights}")
        print(f"  Maximum gold: {result}")
        print()
