def binary_search(K, q):
    minIndex = 0
    maxIndex = len(K) - 1

    while minIndex <= maxIndex:
        midIndex = (minIndex + maxIndex) // 2
        if K[midIndex] == q:
            return midIndex
        elif K[midIndex] < q:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex - 1

    return -1


# Example 1
K = [1, 3, 7, 8, 9, 12]
q = 3
print(f"Array: {K}, Searching for: {q}")
print(f"Index of {q}: {binary_search(K, q)}")

# Example 2
K = [1, 3, 7, 8, 9, 12]
q = 10
print(f"Array: {K}, Searching for: {q}")
print(f"Index of {q}: {binary_search(K, q)}")

# Example 3
K = [2, 4, 6, 8, 10, 12, 14, 16]
q = 6
print(f"Array: {K}, Searching for: {q}")
print(f"Index of {q}: {binary_search(K, q)}")

# Example 4
K = [5, 15, 25, 35, 45]
q = 35
print(f"Array: {K}, Searching for: {q}")
print(f"Index of {q}: {binary_search(K, q)}")
