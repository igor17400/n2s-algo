from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l_p = 0
        r_p = 0
        window_sum = 0
        min_len = 1000
        # for r_p in range(len(nums)):
        while True:
            print("----------")
            if l_p >= len(nums) - 1 and r_p >= len(nums) - 1:
                break  # Break the loop if both conditions are met

            if r_p < len(nums) - 1:
                window_sum += nums[r_p]

            if window_sum >= target:
                min_len = min(min_len, r_p - l_p + 1)
                print("l_p: ", l_p)
                print("r_p: ", r_p)
                print("min_len:", min_len)
                print("window_sum: ", window_sum)
                print("*********")

                window_sum -= nums[l_p]
                if window_sum < target:
                    l_p = r_p
                    window_sum = nums[l_p]
                else:
                    l_p += 1
                    min_len = min(min_len, r_p - l_p + 1)

                print("l_p: ", l_p)
                print("r_p: ", r_p)
                print("min_len:", min_len)
                print("window_sum: ", window_sum)
            elif r_p > len(nums) - 2:
                l_p += 1

            if r_p < len(nums) - 1:
                r_p += 1
            print("----------")

        return min_len if min_len != 1000 else 0


if __name__ == "__main__":
    sol = Solution()

    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    # nums = [1, 1, 1, 1, 1, 1, 1, 1]
    # target = 11

    # nums = [1, 4, 4]
    # target = 4

    # nums = [1, 2, 3, 4, 5]
    # target = 11

    print(sol.minSubArrayLen(target, nums))
