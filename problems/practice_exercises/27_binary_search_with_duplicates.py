def binary_search(keys, query):
    left, right = 0, len(keys) - 1
    result = -1

    # Modified binary search to find the first occurrence
    while left <= right:
        mid = (left + right) // 2
        if keys[mid] == query:
            result = mid  # Record the index and keep searching to the left
            right = mid - 1
        elif keys[mid] < query:
            left = mid + 1
        else:
            right = mid - 1

    return result


# Static Examples for Testing

# Example 1: Array with unique elements, query is present
keys = [1, 3, 5, 7, 9, 11, 13]
queries = [5, 7, 1]
print(f"Array: {keys}, Queries: {queries}")
print(
    f"Results: {[binary_search(keys, q) for q in queries]}\n"
)  # Expected output: [2, 3, 0]

# Example 2: Array with duplicates, query is present multiple times
keys = [2, 4, 4, 4, 6, 8, 8, 10]
queries = [4, 8, 2]
print(f"Array: {keys}, Queries: {queries}")
print(
    f"Results: {[binary_search(keys, q) for q in queries]}\n"
)  # Expected output: [1, 5, 0]

# Example 3: Query not present in the array
keys = [1, 2, 3, 4, 5, 6, 7]
queries = [10, -1, 8]
print(f"Array: {keys}, Queries: {queries}")
print(
    f"Results: {[binary_search(keys, q) for q in queries]}\n"
)  # Expected output: [-1, -1, -1]

# Example 4: Array with a single element, query matches the element
keys = [15]
queries = [15]
print(f"Array: {keys}, Queries: {queries}")
print(f"Results: {[binary_search(keys, q) for q in queries]}\n")  # Expected output: [0]

# Example 5: Array with a single element, query does not match the element
keys = [20]
queries = [15]
print(f"Array: {keys}, Queries: {queries}")
print(
    f"Results: {[binary_search(keys, q) for q in queries]}\n"
)  # Expected output: [-1]

# Example 6: Empty array
keys = []
queries = [1, 2, 3]
print(f"Array: {keys}, Queries: {queries}")
print(
    f"Results: {[binary_search(keys, q) for q in queries]}\n"
)  # Expected output: [-1, -1, -1]

# Example 7: Large array, query is at the beginning
keys = [i for i in range(0, 100, 2)]  # [0, 2, 4, 6, ..., 98]
queries = [0, 98]
print(f"Array: {keys}, Queries: {queries}")
print(
    f"Results: {[binary_search(keys, q) for q in queries]}\n"
)  # Expected output: [0, 49]

# Example 8: Large array, query is at the end
keys = [i for i in range(0, 100, 2)]  # [0, 2, 4, 6, ..., 98]
queries = [98]
print(f"Array: {keys}, Queries: {queries}")
print(
    f"Results: {[binary_search(keys, q) for q in queries]}\n"
)  # Expected output: [49]

# Example 9: Large array, query not present
keys = [i for i in range(0, 100, 2)]  # [0, 2, 4, 6, ..., 98]
queries = [99]
print(f"Array: {keys}, Queries: {queries}")
print(
    f"Results: {[binary_search(keys, q) for q in queries]}\n"
)  # Expected output: [-1]

# Example 10: Array with all elements the same
keys = [7, 7, 7, 7, 7, 7, 7]
queries = [7]
print(f"Array: {keys}, Queries: {queries}")
print(f"Results: {[binary_search(keys, q) for q in queries]}\n")  # Expected output: [0]
