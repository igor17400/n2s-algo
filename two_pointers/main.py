def is_palindrome(word):  # O(n)
	"""
	Check if an array is palindrome
	"""
	l_, r_ = 0, len(word) - 1
	while l_ < r_:
		if word[l_] != word[r_]:
			return False
		l_ += 1
		r_ -= 1
	return True


def target_sum(lst, target):  # O(n)
	"""
	Given a sorted input array, return the two indices of 
	two elements which sums up to the target value. 
	Assume there's exactly one solution.
	"""
	l_, r_ = 0, len(lst) - 1
	while l_ < r_:
		if lst[l_] + lst[r_] > target:
			r_ -= 1
		elif lst[l_] + lst[r_] < target:
			l_ += 1
		else:
			return [l_, r_]


word1 = [1, 2, 3, 3, 2, 1]
word2 = [1, 2, 5, 3, 2, 1]
print(is_palindrome(word1))
print(is_palindrome(word2))

print("---------------")
target = 15
lst = [-3, -2, 0, 3, 6, 9, 11]
print(target_sum(lst, target))
