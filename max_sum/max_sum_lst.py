import math as m


def brute_force(lst):  # O(n^2)
	max_sum = 0
	for i in range(len(lst)):
		for j in range(i, len(lst) + 1):
			sum_ = sum(lst[i:j])
			if sum_ > max_sum:
				max_sum = sum_
	return max_sum


def kadane(lst):  # O(n)
	max_sum, curr_sum = lst[0], -m.inf
	for el in lst:
		curr_sum = max(curr_sum, 0)
		curr_sum += el 
		max_sum = max(max_sum, curr_sum)
	return max_sum


def sliding_window(lst):  # O(n)
	max_sum, curr_sum = lst[0], 0
	max_l, max_r = 0, 0
	l_ = 0

	for r_ in range(len(lst)):
		if curr_sum < 0:
			curr_sum = 0
			l_ = r_

		curr_sum += lst[r_]
		if curr_sum > max_sum:
			max_sum = curr_sum
			max_l, max_r = l_, r_

	return max_sum, max_l, max_r


# lst = [4, -1, 2, -7, 3, 1]
lst = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

print(brute_force(lst))
print(kadane(lst))
print(sliding_window(lst))
