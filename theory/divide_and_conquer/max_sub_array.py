def find_max_cross_subarray(lst, low, mid, high):
	"""
	O(n) time
	"""
	left_sum = -10000
	sum = 0
	max_left = 0
	for i in range(mid, low, -1):
		sum += lst[i]
		if sum > left_sum:
			left_sum = sum
			max_left = i

	right_sum = -10000
	sum = 0
	max_right = 0
	for j in range(mid + 1, high):
		sum += lst[j]
		if sum > right_sum:
			right_sum = sum
			max_right = j

	return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(lst, low, high):
	"""
	Devide and conquer part --> O(log n)
	Joinining with the find_max_cross_subarray --> O(n lg(n))
	"""

	if low == high:
		return (low, high, lst[low])
	else:
		mid = (low + high) // 2
		print("mid --> ", mid)

		left_low, left_high, left_sum = find_max_subarray(lst, low, mid)
		right_low, right_high, right_sum = find_max_subarray(lst, mid + 1, high)
		cross_low, cross_high, cross_sum = find_max_cross_subarray(lst, low, mid, high)

		if left_sum >= right_sum and left_sum >= cross_sum:
			return (left_low, left_high, left_sum)
		if right_sum >= left_sum and right_sum >= cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)


if __name__ == "__main__":
	lst = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

	left, right, sum = find_max_subarray(lst, 0, len(lst) - 1)
	print(left, right, sum)
	print("Let's check the result: ")
	print("Array: ", lst[left: right])
	print("Array sum: ", sum)
