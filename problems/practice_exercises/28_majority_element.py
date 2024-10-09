def majority_element(arr):
    count = 0
    candidate = None

    # Find potential candidate using the Boyer-Moore Voting Algorithm
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Verify if the candidate is the majority element
    if arr.count(candidate) > len(arr) // 2:
        return 1
    else:
        return 0


# Static Examples for Testing

# Example 1: Array with a majority element
input_elements = [2, 3, 9, 2, 2]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 1

# Example 2: Array without a majority element
input_elements = [1, 2, 3, 1]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 0

# Example 3: Array with all elements being the same
input_elements = [4, 4, 4, 4, 4]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 1

# Example 4: Single element array
input_elements = [5]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 1

# Example 5: Large array with a clear majority element
input_elements = [7, 7, 7, 7, 3, 3, 7, 2, 7, 7]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 1

# Example 6: Large array without a majority element
input_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 0

# Example 7: Majority element is at the beginning
input_elements = [10, 10, 10, 10, 3, 3, 2, 1]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 1

# Example 8: Majority element is spread out
input_elements = [6, 1, 6, 2, 6, 3, 6, 4, 6, 5]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 1

# Example 9: Array with two equally frequent elements
input_elements = [8, 8, 7, 7]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 0

# Example 10: Array with no majority element and mixed values
input_elements = [9, 12, 15, 9, 12, 12]
print(f"Array: {input_elements}")
print(
    f"Majority Element Present: {majority_element(input_elements)}\n"
)  # Expected output: 0
