from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, min_sum = nums[0], nums[0]
        curr_sum, curr_min = 0, 0
        total_sum = 0

        for el in nums:
            total_sum += el

            curr_sum = max(curr_sum + el, el)
            max_sum = max(max_sum, curr_sum)

            curr_min = min(curr_min + el, el)
            min_sum = min(min_sum, curr_min)

        # Check if the array has at least one positive number
        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum


if __name__ == "__main__":
    nums = [2, -2, 2, 7, 8, 0]
    sol = Solution()
    print(sol.maxSubarraySumCircular(nums))
