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

word1 = [1, 2, 3, 3, 2, 1]
word2 = [1, 2, 5, 3, 2, 1]
print(is_palindrome(word1))
print(is_palindrome(word2))
