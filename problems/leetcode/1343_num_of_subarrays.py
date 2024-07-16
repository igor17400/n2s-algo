from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l_p = 0
        count = 0
        sum_window = 0
        for r_p in range(len(arr)):
            if r_p - l_p > k - 1:
                sum_window -= arr[l_p]
                l_p += 1
            sum_window += arr[r_p]

            if r_p - l_p == k - 1:
                avg = sum_window / k
                if avg >= threshold:
                    count += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    print(sol.numOfSubarrays(arr, k, threshold))
