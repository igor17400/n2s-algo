class PrefixSum:
	"""
	The time complexity to build the initial prefix sum is 
	O(n). However, to calculate a range sum, we will only perform 
	O(1) operations no matter how big the array is. If we don't 
	need the initial array, we can actually overwrite it with its
	prefix sum, which will bring the time complexity to O(1).
	This works because the size of an array's prefix array will 
	always be the same as itself.
	"""

	def __init__(self, lst):
		self.prefix = []
		total = 0
		for el in lst:
			total += el
			self.prefix.append(total)

	def range_sum(self, left, right):
		pre_right = self.prefix[right]
		pre_left = self.prefix[left - 1] if left > 0 else 0
		return (pre_right - pre_left)
