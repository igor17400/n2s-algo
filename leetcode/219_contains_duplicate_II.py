from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l_p = 0
        for r_p in range(len(nums)):
            if r_p - l_p > k:
                window.remove(nums[l_p])
                l_p += 1
            if nums[r_p] in window:
                return True
            window.add(nums[r_p])
        return False


if __name__ == "__main__":
    # nums = [1, 2, 3, 1]
    # k = 3
    # nums = [1, 2, 3, 1, 2, 3]
    # k = 2
    # nums = [1]
    # k = 1
    # nums = [1, 2]
    # k = 2
    # nums = [1, 0, 1, 1]
    # k = 1
    nums = [4, 1, 2, 3, 1, 5]
    k = 3
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))
