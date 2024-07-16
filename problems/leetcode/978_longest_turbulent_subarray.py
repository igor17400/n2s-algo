from typing import List


class Solution:
	def get_signal(self, arr: List[int], k: int) -> int:
		sign = ""
		if arr[k] > arr[k + 1]:
			sign = ">"
		elif arr[k] < arr[k + 1]:
			sign = "<"
		else:
			sign = ""
		return sign

	def maxTurbulenceSize(self, arr: List[int]) -> int:
		if len(arr) == 1:
			return 1

		l_pointer, r_pointer = 0, 1
		prev_signal, current_signal = "", ""
		max_len = 1
		for idx in range(0, len(arr) - 1):
			current_signal = self.get_signal(arr, idx)
			if (current_signal != prev_signal) and (current_signal != "") and (prev_signal != ""):
				r_pointer = idx + 1
			else:
				if arr[idx] == arr[idx + 1]:
					r_pointer = idx + 2
					l_pointer = idx + 2
				else:
					r_pointer = idx + 1
					l_pointer = idx

			max_len = max(max_len, r_pointer - l_pointer + 1)
			prev_signal = current_signal

		return max(max_len, r_pointer - l_pointer + 1)


if __name__ == '__main__':
	sol = Solution()
	# arr = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
	# arr = [37, 199, 199, 296, 257, 248, 115, 31, 273, 176]
	# arr = [100, 100, 100]
	# arr = [4, 5]
	arr = [99, 99]
	print("-------")
	print(sol.maxTurbulenceSize(arr))
	print("-------")
