"""
Find the length of the longest subarray, with the same value in each position.
"""

def longest_sub_array(lst):  # O(n)
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
	

lst = [4, 2, 2, 3, 3, 3]
print(f"List: {lst}")
print(f"Start index: {longest_sub_array(lst)} | Last index: {longest_sub_array(lst)}")
print(f"Size of the longest subarray: {size_longest_sub_array(lst)}")