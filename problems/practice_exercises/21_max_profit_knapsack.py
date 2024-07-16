"""
Given a list of N items, and a backpack with a
limited capacity, return the maximum total profit that 
can be contained in the backpack. The i-th item's profit
is profit[i] and it's weight is weight[i]. Assume you can
only add each item to the bag at most one time. 
"""

# --- Brute force solution
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Where n is number of item


def dfs(profit, weight, capacity):
	return dfs_aux(0, profit, weight, capacity)


def dfs_aux(i, profit, weight, capacity):
	if i >= len(profit):
		return 0

	# Skip item i
	max_profit = dfs_aux(i + 1, profit, weight, capacity)

	# Include item i
	new_capacity = capacity - weight[i]
	if new_capacity > 0:
		p = profit[i] + dfs_aux(i + 1, profit, weight, new_capacity)
		# compute the max
		max_profit = max(max_profit, p)

	return max_profit 

# --- Memoization solution
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Where n is the number of items & m is the capacity.


def memoization(profit, weight, capacity):
	N, M = len(profit), capacity
	cache = [[-1] * (M + 1) for _ in range(N)]  # save our maximum profit
	return memo_aux(0, profit, weight, capacity, cache)


def memo_aux(i, profit, weight, capacity, cache):
	if i >= len(profit):
		return 0

	# Query in cache
	if cache[i][capacity] != -1:
		return cache[i][capacity]

	# Skip item i
	cache[i][capacity] = dfs_aux(i + 1, profit, weight, capacity)

	# Include item i
	new_capacity = capacity - weight[i]
	if new_capacity > 0:
		p = profit[i] + dfs_aux(i + 1, profit, weight, new_capacity)
		# compute the max
		cache[i][capacity] = max(cache[i][capacity], p)

	return cache[i][capacity] 

# Bottom-Up Solution
# Time: O(n * m)
# Space: O(n * m)
# Where n is the number of items & m is the capacity.


def bottom_up(profit, weight, capacity):
	N, M = len(profit), capacity
	# We want to track the maximum profit we can have for a specific amount of items
	dp = [[0] * (M + 1) for _ in range(N)]

    # Fill the first column and row to reduce edge cases
	for i in range(N):
	    dp[i][0] = 0
	for c in range(M + 1):
	    if weight[0] <= c:
	        dp[0][c] = profit[0]

	# Skip row = 0, we already processed this row before
	for i in range(1, N):
	    for c in range(1, M + 1):
	        skip = dp[i - 1][c]
	        include = 0
	        if c - weight[i] >= 0:
	            include = profit[i] + dp[i - 1][c - weight[i]]
	        dp[i][c] = max(include, skip)

	print("----------")
	print(*(' '.join(str(row)) for row in dp), sep='\n')
	print("----------")
	return dp[N - 1][M]


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8

print(dfs(profit, weight, capacity))
print(memoization(profit, weight, capacity))
print(bottom_up(profit, weight, capacity))
