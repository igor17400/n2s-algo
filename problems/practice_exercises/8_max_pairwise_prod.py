"""
Given an integer \( n \) and a sequence of \( n \) non-negative integers, 
find the maximum value that can be obtained by multiplying two different 
elements from the sequence.
"""
import random

def find_max_pairwise_product(n):
    # Creating list for operations
	lst = [
		random.randint(0, n) for _ in range(n)
	]
	print(f"List: {lst}")
	
	max_prod = 0
	# two-pointer approach
	for i in range(n):
		for j in range(i+1, n):
			max_prev = max_prod
			max_prod = max(max_prod, lst[i]*lst[j])
			if max_prev != max_prod:
				el1 = lst[i]
				el2 = lst[j]
	
	print(f"Element 1: {el1}")
	print(f"Element 2: {el2}")
	print(f"Max product: {max_prod}")
	return max_prod

if __name__ == '__main__':
	find_max_pairwise_product(n = 15)