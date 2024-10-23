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

Given an array, determine if there exist two elements within a window of size $ k $ that are equal. Return `true` if such elements exist, otherwise return `false`.


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

## 7 - Sum Of Two Digits (UCSD Coursera)

### *Problem Statement*:

Compute the sum of two single digit numbers.

### *Path*:
`problems/practice_exercises/7_sum_of_two_digits.py`

## 8 - Maximum Pairwise Product (UCSD Coursera)

### *Problem Statement*:

Given an integer $ n $ and a sequence of $ n $ non-negative integers, find the maximum value that can be obtained by multiplying two different elements from the sequence.

### *Path*:
`problems/practice_exercises/8_max_pairwise_prod.py`

## 9 - Fibonacci Number (UCSD Coursera)

### *Problem Statement*:

Compute the n-th Fibonacci number.

### *Path*:
`problems/practice_exercises/9_fibonacci_number.py`

## 10 - Last Digit Fibonacci Number (UCSD Coursera)

### *Problem Statement*:

Last Digit of Fibonacci Number Problem Compute the last digit of the `n-th` Fibonacci number`

**Input**: An integer 

**Output**: The last digit of the n-th Fibonacci number.

### *Path*:
`problems/practice_exercises/10_last_digit_fibonacci_number.py`

## 11 - Huge Fibonacci Number (UCSD Coursera)

### *Problem Statement*:

Compute the n-th Fibonacci number modulo m.

**Input**: Integers `n` and `m`

**Output**: `n-th` Fibonacci number modulo `m`.

### *Path*:
`problems/practice_exercises/11_huge_fibonacci_number.py`

## 12 - Last Digit of the Sum of Fibonacci Numbers (UCSD Coursera)

### *Problem Statement*:

Compute the last digit of `F0 +F1 +···+Fn`.

**Input**: An integer `n`

**Output**: The last digit of `F0 + F1 + ···+Fn`.

### *Path*:
`problems/practice_exercises/12_last_digit_sum_fibo.py`

## 13 - Last Digit of the Partial Sum of Fibonacci Numbers (UCSD Coursera)

### *Problem Statement*:

Compute the last digit of `Fm +Fm+1 +···+Fn.`.

**Input**: Integers `m ≤ n`.

**Output**: The last digit of `Fm + Fm+1 +···+Fn`.

### *Path*:
`problems/practice_exercises/13_last_digit_partial_sum_fibo.py`

## 14 - Last Digit of the Sum of Squares of Fibonacci Numbers (UCSD Coursera)

### *Problem Statement*:

Compute the last digit of `F0^2 +F1^2 +···+Fn^2`

**Input**: An integer `n`.

**Output**: The last digit of `F0^2 +F1^2 +···+Fn^2`

### *Path*:
`problems/practice_exercises/14_last_digit_sum_square_fibo_num.py`

## 15 - Greates Common Divisor (UCSD Coursera)

### *Problem Statement*:

Compute the greatest common divisor of two positive integers.

**Input**: Two positive integers `a` and `b`.

**Output**: The greatest common divisor of `a` and `b`.

### *Path*:
`problems/practice_exercises/15_gcd.py`

## 16 - Least Common Multiple (UCSD Coursera)

### *Problem Statement*:

Compute the least common multiple of two positive integers.

**Input**: Two positive integers `a` and `b`.

**Output**: The least common multiple of `a` and `b`.

### *Path*:
`problems/practice_exercises/16_lcm.py`

## 17 - Money Change (UCSD Coursera)

### *Problem Statement*:

Compute the minimum number of coins needed to change the given value into coins with de- nominations 1, 5, and 10.

**Input**: An integer money.

**Output**: The minimum number of coins with denominations 1, 5, and 10 that changes money.

## 18 - Maximum Value of the Loot (UCSD Coursera)

### *Problem Statement*:

Find the maximal value of items that fit into the backpack.

**Input:** 
- The capacity of a backpack $ W $ 
- The weights $(w_1, \ldots, w_n)$ 
- The costs $(c_1, \ldots, c_n)$ of $ n $ different compounds.

**Output:**
- The maximum total value of fractions of items that fit into the backpack of the given capacity. 
- The goal is to maximize the value of $ c_1 \cdot f_1 + \cdots + c_n \cdot f_n $ such that $ w_1 \cdot f_1 + \cdots + w_n \cdot f_n \leq W $ and $ 0 \leq f_i \leq 1 $ for all $ i $. Here, $ f_i $ is the fraction of the $ i $-th item taken into the backpack.


### *Path*:
`problems/practice_exercises/18_max_backpack.py`

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


## 23 - Car Fueling (UCSD)

### *Problem Statement*:

Compute the minimum number of gas tank refills needed to travel from one city to another.

**Input:**
- An integer $ d $ representing the total distance between the cities.
- An integer $ m $ representing the maximum distance a car can travel on a full tank.
- An integer $ n $ representing the number of gas stations along the way.
- A sequence of integers $ \text{stop}_1, \text{stop}_2, \ldots, \text{stop}_n $ representing the distances of the gas stations from the starting point, in increasing order.

**Output:**
- The minimum number of refills needed to travel from the starting city to the destination.
- If it is not possible to reach the destination, output $-1$.

### *Input Format*:
- The first line contains an integer $ d $.
- The second line contains an integer $ m $.
- The third line specifies an integer $ n $.
- The last line contains integers $ \text{stop}_1, \text{stop}_2, \ldots, \text{stop}_n $.

### *Output Format*:
- The minimum number of refills needed.
- If it is not possible to reach the destination, output $-1$.

### *Constraints*:
- $ 1 \leq d \leq 10^5 $
- $ 1 \leq m \leq 400 $
- $ 1 \leq n \leq 300 $
- $ 0 < \text{stop}_1 < \text{stop}_2 < \cdots < \text{stop}_n < d $

### *Example*:

**Input:**
```
950
400
4
200 375 550 750
```

**Output:**
```
2
```

**Explanation**:
- The total distance is 950 miles.
- The car can travel a maximum of 400 miles on a full tank.
- There are 4 gas stations at distances 200, 375, 550, and 750 miles.
- The car needs to refill at 200 miles and 550 miles to reach the destination.

### *Path*:

`problems/practice_exercises/23_car_fueling.py`

## 24 - Maximum Advertisement Revenue (UCSD)

### *Problem Statement*:

Find the maximum dot product of two sequences of numbers.

You have $ n = 3 $ advertisement slots on your popular Internet page and you want to sell them to advertisers. They expect, respectively, $ clicks1 = 10 $, $ clicks2 = 20 $, and $ clicks3 = 30 $ clicks per day. You found three advertisers willing to pay $ price1 = \$2 $, $ price2 = \$3 $, and $ price3 = \$5 $ per click. How would you pair the slots and advertisers to maximize the revenue? For example, $ 10 \cdot 5 + 20 \cdot 2 + 30 \cdot 3 = 180 $ gives a revenue of 180 dollars, while $ 10 \cdot 3 + 20 \cdot 5 + 30 \cdot 2 = 190 $ gives a revenue of 190 dollars.

### *Input*:
- Two sequences of $ n $ positive integers: $ price1, price2, \ldots, price_n $ and $ clicks1, clicks2, \ldots, clicks_n $.

### *Output*:
- The maximum value of $ price1 \cdot c1 + price2 \cdot c2 + \ldots + price_n \cdot c_n $, where $ c1, c2, \ldots, c_n $ is a permutation of $ clicks1, clicks2, \ldots, clicks_n $.

### *Input Format*:
- The first line contains an integer $ n $.
- The second line contains a sequence of integers $ price1, price2, \ldots, price_n $.
- The third line contains a sequence of integers $ clicks1, clicks2, \ldots, clicks_n $.

### *Output Format*:
- Output the maximum value of $ (price1 \cdot c1 + price2 \cdot c2 + \ldots + price_n \cdot c_n) $, where $ c1, c2, \ldots, c_n $ is a permutation of $ clicks1, clicks2, \ldots, clicks_n $.

### *Constraints*:
- $ 1 \leq n \leq 10^3 $
- $ 0 \leq price_i, clicks_i \leq 10^5 $ for all $ 1 \leq i \leq n $.

### *Example*:

**Input:**
```
3
1 3 5
2 4 6
```

**Output:**
```
44
```

### *Path*:

`problems/practice_exercises/24_maximum_advertisement_revenue.py`


Here is the markdown code formatted as per the specified format:

## 25 - Collecting Signatures (UCSD)

### *Problem Statement*:

Find the minimum number of points needed to cover all given segments on a line.

You are responsible for collecting signatures from all tenants in a building. For each tenant, you know a period of time when he or she is at home. You would like to collect all signatures by visiting the building as few times as possible. For simplicity, we assume that when you enter the building, you instantly collect the signatures of all tenants that are in the building at that time.

### *Input*:
- A sequence of $ n $ segments $[l_1, r_1], ..., [l_n, r_n]$ on a line.

### *Output*:
- A set of points of minimum size such that each segment $[l_i, r_i]$ contains a point, i.e., there exists a point $ x $ from this set such that $ l_i \leq x \leq r_i $.

### *Input Format*:
- The first line of the input contains the number $ n $ of segments.
- Each of the following $ n $ lines contains two integers $ l_i $ and $ r_i $ (separated by a space) defining the coordinates of endpoints of the $ i $-th segment.

### *Output Format*:
- The minimum number $ k $ of points on the first line and the integer coordinates of $ k $ points (separated by spaces) on the second line. You can output the points in any order. If there are multiple such sets of points, you can output any of them.

### *Constraints*:
- $ 1 \leq n \leq 100 $
- $ 0 \leq l_i \leq r_i \leq 10^9 $ for all $ i $.

### *Example*:

**Input:**
```
3
1 3
2 5
3 6
```

**Output:**
```
1
3
```

### *Path*:

`problems/practice_exercises/25_collecting_signatures.py`

## 26 - Binary Search (UCSD)

### *Problem Statement*:

Search for a key in a sorted array of distinct integers.

### *Input*:
- A sorted array $ K = [k_0, ..., k_{n-1}] $ of distinct integers (i.e., $ k_0 < k_1 < \cdots < k_{n-1} $) and an integer $ q $.

### *Output*:
- Check whether $ q $ occurs in $ K $. If it occurs, return its index. If it does not occur, return -1.

### *Input Format*:
- The first line contains the number of elements $ n $.
- The second line contains $ n $ distinct integers, sorted in increasing order.
- The third line contains the integer $ q $ to be searched for.

### *Output Format*:
- Output the index of $ q $ if it is present in the array. If $ q $ is not present, output -1.

### *Constraints*:
- $ 1 \leq n \leq 3 \times 10^4 $.
- $ -10^9 \leq k_i, q \leq 10^9 $.

### *Example*:

**Input:**
```
6
1 3 7 8 9 12
3
```

**Output:**
```
1
```

### *Path*:

`problems/practice_exercises/26_binary_search.py`


## 27 - Binary Search with Duplicates (UCSD)

### *Problem Statement*:

Find the index of the first occurrence of a key in a sorted array.

### *Input*:
- A sorted array $ K = [k_0, ..., k_{n-1}] $ of integers (possibly with duplicates) and an integer $ q $.

### *Output*:
- Index of the first occurrence of $ q $ in the array, or `-1` if $ q $ does not appear in the array.

### *Input Format*:
- The first line contains the number of elements $ n $.
- The second line contains $ n $ integers, sorted in non-decreasing order.
- The third line contains the integer $ q $ to be searched for.

### *Output Format*:
- Output the index of the first occurrence of $ q $ if it is present in the array. If $ q $ is not present, output `-1`.

### *Constraints*:
- $ 1 \leq n \leq 3 \times 10^4 $.
- $ 1 \leq k_i, q \leq 10^9 $.

### *Example*:

**Input:**
```
7
2 4 4 4 7 7 9
4
```

**Output:**
```
1
```

### *Path*:

`problems/practice_exercises/27_binary_search_with_duplicates.py`


## 28 - Majority Element (UCSD)

### *Problem Statement*:

Check whether a given sequence of numbers contains an element that appears more than half of the times.

### *Input*:
- A sequence of $ n $ integers.

### *Output*:
- `1` if there is an element that is repeated more than $ n/2 $ times, and `0` otherwise.

### *Input Format*:
- The first line contains an integer $ n $.
- The second line contains $ n $ non-negative integers $ a_0, \ldots, a_{n-1} $.

### *Output Format*:
- Output `1` if the sequence contains an element that appears more than $ n/2 $ times, and `0` otherwise.

### *Constraints*:
- $ 1 \leq n \leq 10^5 $.
- $ 0 \leq a_i \leq 10^9 $ for all $ 0 \leq i < n $.

### *Example*:

**Input:**
```
5
2 3 9 2 2
```

**Output:**
```
1
```

**Input:**
```
4
1 2 3 1
```

**Output:**
```
0
```

### *Path*:

`problems/practice_exercises/28_majority_element.py`


## 29 - Speeding-up Randomized QuickSort (UCSD)

### *Problem Statement*:

Sort a given sequence of numbers (that may contain duplicates) using a modification of **Randomized QuickSort** that works in $O(n \log n)$ expected time.

### *Input*:
- An integer array with $ n $ elements that may contain duplicates.

### *Output*:
- Sorted array (generated using a modification of **Randomized QuickSort**) that works in $ O(n \log n) $ expected time.

### *Input Format*:
- The first line of the input contains an integer $ n $.
- The second line contains a sequence of $ n $ integers $ a_0, a_1, \ldots, a_{n-1} $ in non-decreasing order.

### *Output Format*:
- Output the sequence sorted in non-decreasing order.

### *Constraints*:
- $ 1 \leq n \leq 10^5 $.
- $ 1 \leq a_i \leq 10^9 $ for all $ 0 \leq i < n $.

### *Example*:

**Input:**
```
5
2 3 9 2 2
```

**Output:**
```
2 2 2 3 9
```

### *Path*:

`problems/practice_exercises/29_speeding_up_randomized_quicksort.py`


## 30 - Number of Inversions (UCSD)

### *Problem Statement*:

Compute the number of inversions in a sequence of integers.

An **inversion** in a sequence measures how close the sequence is to being sorted. An inversion occurs when there are two indices $i, j$ such that $i < j$ and $a_i > a_j$. 

For example, a sequence sorted in the non-descending order has no inversions, while a sequence sorted in descending order has $ n(n - 1)/2 $ inversions (where $ n $ is the number of elements in the sequence).

### *Input*:
- A sequence of $ n $ integers: $ a_1, a_2, \ldots, a_n $.

### *Output*:
- The number of inversions in the sequence, i.e., the number of pairs $ (i, j) $ such that $ i < j $ and $ a_i > a_j $.

### *Input Format*:
- The first line contains an integer $ n $, the next line contains a sequence of $ n $ integers $ a_1, a_2, \ldots, a_n $.

### *Output Format*:
- A single integer representing the number of inversions in the sequence.

### *Constraints*:
- $ 1 \leq n \leq 30,000 $.
- $ 1 \leq a_i \leq 10^9 $ for all $ 1 \leq i \leq n $.

### *Example*:

**Input:**
```
5
2 3 9 2 9
```

**Output:**
```
2
```

**Explanation:**  
The two inversions are:
- $ (2, 4) $ because $ a_2 = 3 > 2 = a_4 $.
- $ (3, 4) $ because $ a_3 = 9 > 2 = a_4 $.

### *Path*:

`problems/practice_exercises/30_number_of_inversions.py`

## 31 - Money Change Again (Dynamic Programming - UCSD)

### *Problem Statement*:
Given a value `money`, compute the minimum number of coins needed to change the given value into coins with denominations 1, 3, and 4.

### *Input*:
- An integer `money` representing the value to be changed.

### *Output*:
- The minimum number of coins with denominations 1, 3, and 4 that change `money`.

### *Input Format*:
- A single integer representing the value `money`.

### *Output Format*:
- A single integer representing the minimum number of coins required.

### *Constraints*:
- $1 \leq \text{money} \leq 1000$.

### *Example*:

**Input:**
```
34
```

**Output:**
```
9
```

**Explanation:**  
34 can be changed using nine coins: $3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4$.

### *Approach*:
To solve this problem, we will use dynamic programming. We define an array `min_coins` where `min_coins[i]` stores the minimum number of coins required to make change for the amount `i`. We initialize the base case `min_coins[0] = 0` since zero coins are needed to make the amount zero.

For each value from `1` to `money`, we find the minimum number of coins by checking the denominations 1, 3, and 4 and updating the `min_coins` array. The recurrence relation used is:

$$
\text{min\_coins}[i] = \min(\text{min\_coins}[i - c] + 1) \quad \text{for each } c \in \{1, 3, 4\}
$$

### *Path*:
`problems/dynamic_programming/31_money_change_again.py`

## 32 - Primitive Calculator (Dynamic Programming - UCSD)

### *Problem Statement*:
Given a positive integer `n`, find the minimum number of operations needed to reach `n` starting from `1` using only three operations:
- Add 1 to the current number.
- Multiply the current number by 2.
- Multiply the current number by 3.

### *Input*:
- A single integer `n` representing the target number.

### *Output*:
1. The minimum number of operations required to get from 1 to `n`.
2. A sequence of intermediate numbers starting from `1` and ending at `n` using the minimum number of operations.

### *Input Format*:
- A single positive integer `n`.

### *Output Format*:
- The first line should contain an integer representing the minimum number of operations required.
- The second line should contain a sequence of positive integers starting from `1` and ending at `n` such that each integer is either:
  - The previous integer plus 1,
  - Twice the previous integer,
  - Three times the previous integer.

### *Constraints*:
- $1 \leq n \leq 10^6$.

### *Example*:

**Input:**
```
96234
```

**Output:**
```
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
```

**Explanation:**  
The optimal sequence involves 14 operations starting from `1` and applying the allowed operations to reach `96234`. One possible sequence is `1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234`.

### *Approach*:
To solve this problem efficiently, we will use dynamic programming to compute the minimum number of operations and backtrack to determine the sequence of operations. We'll create an array `min_ops` where `min_ops[i]` stores the minimum number of operations needed to reach `i` from `1`. For each number, we'll evaluate the three possible operations and keep track of the optimal path.

### *Path*:
`problems/dynamic_programming/32_primitive_calculator.py`

## 33 - Edit Distance (Dynamic Programming - UCSD)

### *Problem Statement*:
Compute the **edit distance** between two strings. The **edit distance** is defined as the minimum number of single-symbol insertions, deletions, and substitutions required to transform one string into the other.

### *Input*:
- Two strings consisting of lower-case Latin letters, each provided on a separate line.

### *Output*:
- The minimum number of single-symbol insertions, deletions, and substitutions required to transform one string into the other.

### *Example*:

**Input:**
```
short
ports
```

**Output:**
```
3
```

**Explanation:**  
The second string can be obtained from the first one by deleting 's', substituting 'h' for 'p', and inserting 's'.  
The alignment of operations is:

```
short
p o r t s
```

### *Approach*:
To solve this problem, we will use **dynamic programming**. We create a 2D array `dp` where `dp[i][j]` represents the edit distance between the first `i` characters of the first string and the first `j` characters of the second string.  
The recurrence relation used is:

\[
dp[i][j] = 
\begin{cases} 
dp[i-1][j-1] & \text{if } s1[i-1] = s2[j-1] \\
1 + \min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) & \text{if } s1[i-1] \neq s2[j-1}
\end{cases}
\]

Where:
- `dp[i-1][j]` represents a **deletion**,
- `dp[i][j-1]` represents an **insertion**,
- `dp[i-1][j-1]` represents a **substitution**.

### *Path*:
`problems/dynamic_programming/33_edit_distance.py`

## 34 - Longest Common Subsequence of Two Sequences (Dynamic Programming - UCSD)

### *Problem Statement*:
Compute the maximum length of a common subsequence between two sequences. The **Longest Common Subsequence (LCS)** problem is defined as finding the longest subsequence common to both sequences, where a **subsequence** is a sequence derived by deleting zero or more elements from the original sequence without changing the order of the remaining elements.

### *Input*:
- Two sequences `A = (a1, a2, ..., an)` and `B = (b1, b2, ..., bm)`.

### *Output*:
- The maximum length of a common subsequence.

### *Input Format*:
1. The first line contains an integer `n`, the length of the first sequence.
2. The second line contains `n` integers representing the elements of the first sequence.
3. The third line contains an integer `m`, the length of the second sequence.
4. The fourth line contains `m` integers representing the elements of the second sequence.

### *Output Format*:
- A single integer `p` representing the length of the longest common subsequence.

### *Constraints*:
- $1 \leq n, m \leq 100$.
- Each element of the sequences is a positive integer.

### *Example*:

**Input:**
```
5
7 2 9 3 1
7
2 8 1 3 9 7
```

**Output:**
```
3
```

**Explanation:**  
The longest common subsequence between the two sequences is `[2, 3, 7]` with length 3.

### *Approach*:
We will use **dynamic programming** to solve this problem efficiently. We define a 2D array `dp` where `dp[i][j]` represents the length of the longest common subsequence between the first `i` elements of sequence `A` and the first `j` elements of sequence `B`.  
The recurrence relation used is:

\[
dp[i][j] = 
\begin{cases} 
dp[i-1][j-1] + 1 & \text{if } a_{i} = b_{j} \\
\max(dp[i-1][j], dp[i][j-1]) & \text{if } a_{i} \neq b_{j}
\end{cases}
\]

### *Path*:
`problems/dynamic_programming/34_longest_common_subsequence.py`

## 35 - Maximum Amount of Gold (Dynamic Programming - UCSD)

### *Problem Statement*:
Given a set of gold bars of various weights and a backpack that can hold at most W pounds, determine the maximum amount of gold that can be placed into the backpack. This is a variation of the classic 0/1 Knapsack problem.

### *Input*:
- An integer W representing the capacity of the backpack.
- An integer n representing the number of gold bars.
- A sequence of n integers w1, ..., wn representing the weights of the gold bars.

### *Output*:
- The maximum total weight of gold bars that fit into a backpack of capacity W.

### *Input Format*:
1. The first line contains two integers W and n, separated by a space.
2. The second line contains n integers w1, ..., wn, separated by spaces, representing the weights of the gold bars.

### *Output Format*:
- A single integer representing the maximum weight of gold that fits into the backpack.

### *Constraints*:
- $1 \leq W \leq 10^4$
- $1 \leq n \leq 300$
- $0 \leq w_1, ..., w_n \leq 10^5$

### *Example*:

**Input:**
```
10 3
1 4 8
```

**Output:**
```
9
```

**Explanation:**  
The optimal solution is to take the first and the last bar (weights 1 and 8) for a total weight of 9.

### *Approach*:
We will use **dynamic programming** to solve this problem efficiently. We define a 2D array `dp` where `dp[i][w]` represents the maximum value of gold that can be obtained using the first `i` items and a capacity of `w`.  
The recurrence relation used is:

\[
dp[i][w] = 
\begin{cases} 
\max(dp[i-1][w], dp[i-1][w-weights[i-1]] + weights[i-1]) & \text{if } weights[i-1] \leq w \\
dp[i-1][w] & \text{if } weights[i-1] > w
\end{cases}
\]

### *Path*:
`/problems/dynamic_programming/35_max_amount_of_gold.py`

## 36 - Splitting the Pirate Loot (UCSD)

### Problem Description
Three pirates are trying to split their loot consisting of n items of varying value. This program helps determine if it's possible to evenly split the loot into three subsets with equal sums.

#### Input
- The first line contains an integer n (1 ≤ n ≤ 20), representing the number of items.
- The second line contains n integers v1, v2, ..., vn (1 ≤ vi ≤ 30), representing the values of the items.

#### Output
- Output 1 if it's possible to partition v1, v2, ..., vn into three subsets with equal sums, and 0 otherwise.

#### Constraints
- 1 ≤ n ≤ 20
- 1 ≤ vi ≤ 30 for all i

## Example

**Input:**
```
4
3 3 3 3
```

**Output:**
```
0
```


# References:

- https://www.coursera.org/specializations/data-structures-algorithms
- https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/


