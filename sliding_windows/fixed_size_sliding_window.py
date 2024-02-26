"""
Given an array, return true if there are two elements within a window 
of size k that are equal.
"""


def close_duplicates_brute_force(lst, k):  # O(n^2)
	for l_ in range(len(lst)):
		for r_ in range(l_ + 1, min(len(lst), l_ + k)):
			if lst[l_] == lst[r_]:
				return true
	return False


def close_duplicates(lst, k):  # O(n)
	"""
	Rolling hash windows.
	Getting an element from the window is O(1)
	"""
	window = set()  # current window of size <= k
	l_ = 0

	for r_ in range(len(lst)):
		if r_ - l_ + 1 > k:
			window.remove(lst[l_])
			l_ += 1
		if lst[r_] in window:
			return True
		window.add(lst[r_])
	return False
