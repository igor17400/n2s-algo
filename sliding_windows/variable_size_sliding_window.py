import math as m


def longest_sub_array(lst):  # O(n)
	"""
	Find the length of the longest subarray, with the same value in each position.
	"""
	l_, r_ = 0, 0
	max_l, max_r = 0, 0
	while r_ < len(lst):
		if lst[l_] == lst[r_]:
			if (max_r - max_l) < r_ - l_:
				max_l, max_r = l_, r_
			r_ += 1
		else:
			l_ = r_

	return (max_l, max_r)


def size_longest_sub_array(lst):  # O(n)
	"""
	Return the size of the longest subarray, with the same value in each position
	"""
	l_ = 0
	length = 0
	for r_ in range(len(lst)):
		if lst[l_] != lst[r_]:
			l_ = r_
		length = max(length, r_ - l_ + 1)

	return length


def shortest_sub_array(lst, target):  # O(n)
	"""
	Find the minimum length subarray, where the sum is greater than or equal to the target. 
	** Assume all values are positive. **
	keyword: "rolling windows"

	return:

	- l_ : left index
	- r_ : right index
	- length : length of the subarray
	"""
	l_, sum_ = 0, 0
	length = m.inf
	min_l, min_r = -m.inf, -m.inf
	for r_ in range(len(lst)):
		sum_ += lst[r_]
		while sum_ >= target:
			min_l = l_
			min_r = r_
			length = min(r_ - l_ + 1, length)
			sum_ -= lst[l_]
			l_ += 1

	return (0, 0, 0) if length == m.inf else (length, min_l, min_r)


lst = [4, 2, 2, 3, 3, 3]

print(longest_sub_array(lst))
print(size_longest_sub_array(lst))


lst = [2, 3, 1, 2, 4, 3, 3, 0, 0, 0]
lst = [2, 3, 1, 2, 4, 3]

print(shortest_sub_array(lst, target=5))
