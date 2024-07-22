from sys import stdin


def knapsack_01_helper(level, capacity, weights, values):
    if level == len(values):
        return 0

    if weights[level] > capacity:
        return knapsack_01_helper(level + 1, capacity, weights, values)

    profit_with = values[level] + knapsack_01_helper(
        level + 1, capacity - weights[level], weights, values
    )
    profit_without = knapsack_01_helper(level + 1, capacity, weights, values)

    return max(profit_with, profit_without)


def knapsack_01_naive(capacity, weights, values):
    """
    We can only choose 1 element or no element for each kind. This is called
    the 0/1 Knapsack problem.
    """
    profit = 0
    return knapsack_01_helper(0, capacity, weights, values)


if __name__ == "__main__":
    # lst = [[3, 50, 60, 20, 100, 50, 120, 30], [1, 10, 500, 30]]
    lst = [[4, 8, 4, 5, 4, 2, 7, 3, 1, 1], [3, 50, 60, 10, 100, 20, 120, 30], [4, 7, 10, 1, 40, 3, 50, 4, 70, 5]]
    response = [9, 220, 90]

    for idx, data in enumerate(lst):
        n, capacity = data[0:2]
        values = data[2 : (2 * n + 2) : 2]
        weights = data[3 : (2 * n + 2) : 2]
        profit = knapsack_01_naive(capacity, weights, values)
        print(f"\nOutput: {profit}")
        print(f"Correct Response: {response[idx]}\n")

    # data = list(map(int, stdin.read().split()))
    # n, capacity = data[0:2]
    # values = data[2:(2 * n + 2):2]
    # weights = data[3:(2 * n + 2):2]
    # opt_value = knapsack(capacity, weights, values)
    # print("{:.10f}".format(opt_value))
