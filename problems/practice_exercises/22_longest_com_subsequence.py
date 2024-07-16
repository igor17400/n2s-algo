"""
LCS - Longest Common Subsequence
"""


"""
Given two strings s1 and s2, find the length of the longest
common subsequence between the two strings.
"""

# --- Recurisve solution
# Time complexity: O(2^(m + n))
# m : number of characters in s1
# n : number of characters in s2


def lcs_recursive(s1, s2, i, j):
	# base case
	if i >= len(s1) or j >= len(s2):
		return 0

	if s1[i] == s2[j]:
		return 1 + lcs_recursive(s1, s2, i + 1, j + 1)
	else:
		return max(lcs_recursive(s1, s2, i + 1, j), lcs_recursive(s1, s2, i, j + 1))


# --- Memoization solution
# Time complexity: O(m * n)
# m : number of characters in s1
# n : number of characters in s2

def lcs_memoization(s1, s2, i, j):
	m = len(s1)
	n = len(s2)
	memo = [[-1] * m for _ in range(n)]

	return lcs_memoization_aux(s1, s2, i, j, memo)


def lcs_memoization_aux(s1, s2, i, j, memo):
	# base case
	if i >= len(s1) or j >= len(s2):
		return 0

	if memo[i][j] != -1:
		return memo[i][j]

	if s1[i] == s2[j]:
		memo[i][j] = 1 + lcs_recursive(s1, s2, i + 1, j + 1)
	else:
		memo[i][j] = max(lcs_recursive(s1, s2, i + 1, j), lcs_recursive(s1, s2, i, j + 1))

	return memo[i][j]

# --- Top to bottom solution
# Time complexity: O(m * n)
# m : number of characters in s1
# n : number of characters in s2


def print_matrix(matrix, row_labels, col_labels):
    # Print the column labels
    print("     ", end="")
    for col_label in col_labels:
        print(f"{col_label:<6}", end="")
    print()

    # Print the matrix with row labels
    for i, row in enumerate(matrix):
        print(f"{row_labels[i]:<5}", end="")
        for element in row:
            print(f"{element:<6}", end="")
        print()


def lcs_top_bottom(s1, s2):
	n, m = len(s1), len(s2)
	# Adding this +1 give us a better way to query into our array
	dp = [[0] * (m + 1) for _ in range(n + 1)]

	print("s1 = ", s1)
	print("s2 = ", s2)

	print("----- initial -----")
	print_matrix(dp, ["-"] + s1, ["-"] + s2)
	print("----------")

	for i in range(n):
		for j in range(m):
			if s1[i] == s2[j]:
				print("String s1[{}]={} with s2[{}]={} matched!".format(i, s1[i], j, s2[j]))
				dp[i + 1][j + 1] = 1 + dp[i][j]
			else:
				dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

		print("----------")
		print_matrix(dp, ["-"] + s1, ["-"] + s2)
		print("----------")

	print("----- final -----")
	print_matrix(dp, ["-"] + s1, ["-"] + s2)
	print("----------")

	return dp[n][m]


s1 = "adcc"
s2 = "abc"

print(lcs_recursive(list(s1), list(s2), 0, 0))
print(lcs_memoization(list(s1), list(s2), 0, 0))
print(lcs_top_bottom(list(s1), list(s2)))
