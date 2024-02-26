"""
r_n = max(p_i + r_{n-i}) for 0 <= i <= n
"""
import math as m


def memoized_cut_rod(p, n):
	"""
	p: price list
	"""
	memo = [-m.inf] * (n + 1)

	return memoized_aux_cut_rod(p, n, memo)


def memoized_aux_cut_rod(p, n, memo):
	if memo[n - 1] >= 0:
		return memo[n - 1]

	if n == 0:
		q = 0

	else:
		q = -m.inf
		for i in range(1, n + 1):
			q = max(q, p[i - 1] + memoized_aux_cut_rod(p, n - i, memo))

	memo[n - 1] = q
	return q


def bottom_up_cut_rod(p, n):
	"""
	p: price list
	n: number of possible cuts
	"""
	memo = [-m.inf] * (n + 1)
	memo[0] = 0

	for i in range(1, n + 1):
		q = -m.inf
		for j in range(1, i + 1):
			q = max(q, p[j - 1] + memo[i - j])
		memo[i] = q
	return memo[n]


p = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8

print(memoized_cut_rod(p, n))
print(bottom_up_cut_rod(p, n))
