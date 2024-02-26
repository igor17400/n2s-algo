class Solution:
    def kadane(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for el in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += el
            max_sum = max(max_sum, curr_sum)
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        return self.kadane(nums)
