def min_coins_change(money):
    # Denominations available
    coins = [1, 3, 4]

    # Create a DP array to store the minimum number of coins for each amount up to 'money'
    min_coins = [float("inf")] * (money + 1)

    # Base case: 0 money requires 0 coins
    min_coins[0] = 0

    # Fill the DP array using the bottom-up approach
    for m in range(1, money + 1):
        for coin in coins:
            if m >= coin:
                # If we can use the coin, update the minimum number of coins needed
                min_coins[m] = min(min_coins[m], min_coins[m - coin] + 1)

    return min_coins[money]


# Example usage and test cases
if __name__ == "__main__":
    # Static test case from the problem statement
    money = 34
    print(
        f"Minimum number of coins for {money}: {min_coins_change(money)}"
    )  # Expected Output: 9

    # Additional test cases
    test_cases = [6, 10, 12, 17, 100, 999, 1000]
    for test in test_cases:
        print(f"Minimum number of coins for {test}: {min_coins_change(test)}")
