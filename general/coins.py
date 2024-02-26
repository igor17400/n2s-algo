import math as m


def minimum_or_none(a, b):
	if a is None:
		return b
	elif b is None:
		return a
	return min(a, b)


def get_min_lst(lst_a, lst_b):
	if lst_a == []:
		return lst_b
	if lst_b == []:
		return lst_a
	if len(lst_a) < len(lst_b):
		return lst_a
	else:
		return lst_b


def minimum_cost_memoization(m, coins):
	"""
	m: target sum
	coins: array with all the coins we have

	Method with memoization using top-down approach
	"""
	memo_ = {}

	return minimum_cost_memoization_aux(m, coins, memo_)


def minimum_cost_memoization_aux(m, coins, memo_):
	"""
	Top to down approach
	"""
	if m in memo_:
		return memo_.get(m)

	answer = []
	if m != 0:
		answer = []
		for coin in coins:
			subproblem = m - coin
			if subproblem >= 0:
				answer = get_min_lst(answer, minimum_cost_memoization_aux(subproblem, coins, memo_) + [coin])

	memo_[m] = answer
	return memo_.get(m)


def minimum_cost_bottom_up(m, coins):
	"""
	m: target sum
	coins: array with all the coins we have

	Let's implement use the bottom-up approach
	"""

	# Initialize a dictionary to store the least amount of coins for each target value
	dp = {}
	dp[0] = []

	# Iterate through all possible target values up to the given target_sum
	for i in range(1, target_sum + 1):
	    # Initialize the least amount of coins for the current target value
	    min_coins_for_i = float('inf')

	    # Iterate through each coin denomination
	    for coin in coins:
	        # Check if the current coin can be used to reach the current target value
	        subproblem = i - coin
	        if subproblem >= 0 and len(dp[subproblem]) + 1 < min_coins_for_i:
	            # Update the least amount of coins for the current target value
	            min_coins_for_i = len(dp[subproblem]) + 1
	            # Update the solution for the current target value
	            dp[i] = dp[subproblem] + [coin]

	# Return the least amount of coins for the target_sum
	return dp[target_sum]


coins = [1, 4, 5]
target_sum = 13
print(minimum_cost_memoization(target_sum, coins))
print(minimum_cost_bottom_up(target_sum, coins))
