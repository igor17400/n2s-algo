# Problems

This folder contains solutions to various algorithm problems. Below is a list showing the directory path for each problem along with its corresponding question.

# Leetcode

The `leetcode` folder provides solutions to different exercises from the https://leetcode.com/ platform. 

All the descriptions follow the following format:

```
------------
## XX - Problem Description 

### *Problem Statement*:

bla bla bla bla

### *Path*:

`/problems/leetcode/path_to_code`

### *Link*:

https:link_to_problem.com
----------
```

## 53 - Maximum Subarray

### *Problem Statement*

Given an integer array `nums`, find the subarray with the largest sum and return its sum.

### *Path*

`/problems/leetcode/53_maximum_subarray.py`


### *Link*

https://leetcode.com/problems/maximum-subarray/description/


## 80 - Remove Duplicates II

### *Problem Statement*:

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, the result must be placed in the first part of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

**Note:** Do not allocate extra space for another array. Modify the input array in-place with O(1) extra memory.

### *Path*

`/problems/leetcode/53_maximum_subarray.py`

### *Link*

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/


## 209 - Number of subarrays

### *Problem Statement* 

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

### *Path*

`/problems/leetcode/209_min_size_sub_arr_sum.py`

### *Link*

https://leetcode.com/problems/minimum-size-subarray-sum/description/

## 219 - Contains Duplicate II

### *Problem Statement*: 

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0 instead.

### *Path*

`/problems/leetcode/209_min_size_sub_arr_sum.py`

### *Link*: 

https://leetcode.com/problems/minimum-size-subarray-sum/description/ 

## 918 - Maximum Sum Circular Subarray

### *Problem Statement*:

Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray of `nums`.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of `nums[i]` is `nums[(i + 1) % n]` and the previous element of `nums[i]` is `nums[(i - 1 + n) % n]`.

A subarray may only include each element of the fixed buffer `nums` at most once. Formally, for a subarray `nums[i], nums[i + 1], ..., nums[j]`, there does not exist `i <= k1, k2 <= j` with `k1 % n == k2 % n`.

### *Path*:

`/problems/leetcode/918_maximum_sum_circular_subarray.py`

### *Link*:

https://leetcode.com/problems/maximum-sum-circular-subarray/description/

## 978 - Longest Turbulent Subarray

### *Problem Statement*:

Given an integer array `arr`, return the length of a maximum size turbulent subarray of `arr`.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray `[arr[i], arr[i + 1], ..., arr[j]]` of `arr` is said to be turbulent if and only if:

- For `i <= k < j`:
  - `arr[k] > arr[k + 1]` when `k` is odd, and
  - `arr[k] < arr[k + 1]` when `k` is even,
  
  OR
  
- For `i <= k < j`:
  - `arr[k] > arr[k + 1]` when `k` is even, and
  - `arr[k] < arr[k + 1]` when `k` is odd.

### *Path*:

`/problems/leetcode/978_longest_turbulent_subarray.py`

### *Link*:

https://leetcode.com/problems/longest-turbulent-subarray/description/

## 1343 - Number of subarrays

### *Problem Statement*

Given an array of integers `arr` and two integers `k` and `threshold`, return the number of sub-arrays of size `k` and average greater than or equal to `threshold`.

### *Path*

`/problems/leetcode/1343_num_of_subarrays.py`

### *Link*: 

https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/


# Practice Exercises

This directory includes exercises sourced from books, tutorials, and various online references.

## 1 - Maximum Sum

### *Problem Statement*:

Given an array `lst` of integers, find the maximum sum of any contiguous subarray using three different approaches: brute force, Kadane's algorithm, and sliding window.

### *Path*: 

`problems/practice_exercises/1_max_sum.py`

## 2 - Duplicates in Array

### *Problem Statement*: 

Given an array, determine if there exist two elements within a window of size \( k \) that are equal. Return `true` if such elements exist, otherwise return `false`.


### *Path*:

`problems/practice_exercises/2_duplicates_in_array.py`

## 3 - Longest Subarray

### *Problem Statement*:

Find the size and the first and last elements of the longest subarray, with the same value in each position.

### *Path*:

`problems/practice_exercises/3_longest_subarray.py`

## 4 - Minimum Length Subarray Sum

### *Problem Statement*:

Find the minimum length subarray in a given array, where the sum of elements is greater than or equal to a specified target. **Assume all values are positive.** Implement the solution using the "rolling windows" technique.

**Return:**
- `l_`: The left index of the subarray.
- `r_`: The right index of the subarray.
- `length`: The length of the subarray.

### *Path*:

`problems/practice_exercises/4_min_len_subarr_sum.py`

## 5 - Palindrome Array

### *Problem Statement*:

Check if an array is palindrome

### *Path*:

`problems/practice_exercises/5_palindrome.py`

## 6 - Sum Target Value

### *Problem Statement*:

Given a sorted input array, return the two indices of  two elements which sums up to the target value. Assume there's exactly one solution.

### *Path*:

`problems/practice_exercises/6_sum_target_value.py`

## 7 - Sum Of Two Digits

### *Problem Statement*:

Compute the sum of two single digit numbers.

### *Path*:
`problems/practice_exercises/7_sum_of_two_digits.py`

## 8 - Maximum Pairwise Product

### *Problem Statement*:

Given an integer \( n \) and a sequence of \( n \) non-negative integers, find the maximum value that can be obtained by multiplying two different elements from the sequence.

### *Path*:
`problems/practice_exercises/8_max_pairwise_prod.py`

## 19 -  Minimum Coin Change Problem

### *Problem Statement*:

Implement two methods to determine the minimum number of coins needed to reach a target sum `m` using a given set of coin denominations `coins`.

1. **Memoization Approach (`minimum_cost_memoization`):**
   - Uses memoization with a top-down approach to recursively calculate and store solutions for subproblems.
   - Returns a list of the minimum coins needed to achieve the target sum `m`.

2. **Bottom-Up Dynamic Programming Approach (`minimum_cost_bottom_up`):**
   - Implements a bottom-up approach to iteratively compute the minimum coins required for each target value up to `m`.
   - Returns a list of the minimum coins needed to achieve the target sum `m`.


### *Path*:

`problems/practice_exercises/19_minimum_coin_change_problem.py`

## 20 - Maximum Revenue from Rod Cutting

### *Problem Statement*:

Implement two methods to determine the maximum revenue obtainable by cutting a rod of length `n` into pieces, where each piece `i` can be sold for a price `p_i`. The goal is to maximize the revenue by determining the optimal way to cut the rod.

1. **Memoization Approach (`memoized_cut_rod`):**
   - Uses memoization with a recursive approach to store and reuse solutions to subproblems.
   - Returns the maximum revenue obtainable for a rod of length `n`.

2. **Bottom-Up Dynamic Programming Approach (`bottom_up_cut_rod`):**
   - Implements a bottom-up approach to iteratively compute the maximum revenue for rod lengths from `1` to `n`.
   - Returns the maximum revenue obtainable for a rod of length `n`.

This problem aims to find the optimal solution using dynamic programming principles to efficiently compute the maximum revenue from cutting a rod. Adjust the details or add more information as needed for your specific use case or documentation requirements.


### *Path*:

`problems/practice_exercises/20_max_rev_from_rod.py`

## 21 -  Maximum Profit in Knapsack Problem

### Problem Statement:

Given a list of N items, and a backpack with a limited capacity, return the maximum total profit that can be contained in the backpack. Each item `i` has a profit `profit[i]` and a weight `weight[i]`. You can add each item to the bag at most one time.

#### Brute Force Solution
- Time Complexity: O(2^n)
- Space Complexity: O(n)
- Where `n` is the number of items.

#### Memoization Solution
- Time Complexity: O(n * m)
- Space Complexity: O(n * m)
- Where `n` is the number of items and `m` is the capacity of the backpack.

#### Bottom-Up Dynamic Programming Solution
- Time Complexity: O(n * m)
- Space Complexity: O(n * m)
- Where `n` is the number of items and `m` is the capacity of the backpack.

This problem aims to find the optimal solution using dynamic programming principles to efficiently compute the maximum profit that can be obtained by selecting items to fit within the capacity of a knapsack. Adjust the details or add more information as needed for your specific use case or documentation requirements.

### *Path*:

`problems/practice_exercises/20_max_rev_from_rod.py`

## 22 - Longest Common Subsequence (LCS)

### *Problem Statement*:

Given two strings `s1` and `s2`, find the length of the longest common subsequence between the two strings.

### Recursive Solution
- Time Complexity: O(2^(m + n))
- Space Complexity: O(m + n)
- Where `m` is the number of characters in `s1` and `n` is the number of characters in `s2`.

### Memoization Solution
- Time Complexity: O(m * n)
- Space Complexity: O(m * n)
- Where `m` is the number of characters in `s1` and `n` is the number of characters in `s2`.

### Top-Down Dynamic Programming Solution
- Time Complexity: O(m * n)
- Space Complexity: O(m * n)
- Where `m` is the number of characters in `s1` and `n` is the number of characters in `s2`.

This problem aims to find the length of the longest common subsequence between two given strings using various approaches such as recursion with memoization and dynamic programming. Adjust the details or add more information as needed for your specific use case or documentation requirements.

### *Path*:

`problems/practice_exercises/22_longest_com_subsequence.py`


## 1 - 

### *Problem Statement*:

### *Path*:

`problems/practice_exercises/XXXX.py`


# References:

- https://www.coursera.org/specializations/data-structures-algorithms
- https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/


