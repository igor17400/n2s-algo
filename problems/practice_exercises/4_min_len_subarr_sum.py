"""
Find the minimum length subarray in a given array, where the sum 
of elements is greater than or equal to a specified target. 

**Assume all values are positive.** 

Implement the solution using the "rolling windows" technique.
"""
import math as m


def shortest_sub_array(lst, target):  # O(n)
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


lst = [2, 3, 1, 2, 4, 3, 3, 0, 0, 0]
lst = [2, 3, 1, 2, 4, 3]

print(shortest_sub_array(lst, target=5))
