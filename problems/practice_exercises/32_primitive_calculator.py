def primitive_calculator(n):
    # Array to store the minimum number of operations for each number from 1 to n
    min_ops = [0] * (n + 1)

    # Iterate over all numbers from 2 to n to fill the array with the minimum number of operations
    for i in range(2, n + 1):
        # Start with the operation "subtract 1" as the default operation
        min_ops[i] = min_ops[i - 1] + 1

        # Check if divisible by 2 and update the minimum operations if better
        if i % 2 == 0:
            min_ops[i] = min(min_ops[i], min_ops[i // 2] + 1)

        # Check if divisible by 3 and update the minimum operations if better
        if i % 3 == 0:
            min_ops[i] = min(min_ops[i], min_ops[i // 3] + 1)

    # Reconstruct the sequence of operations starting from n
    sequence = []
    while n > 0:
        sequence.append(n)
        # Find the previous number based on the operation that resulted in n
        if n % 3 == 0 and min_ops[n] == min_ops[n // 3] + 1:
            n = n // 3
        elif n % 2 == 0 and min_ops[n] == min_ops[n // 2] + 1:
            n = n // 2
        else:
            n -= 1

    # Reverse the sequence to start from 1
    sequence.reverse()
    return len(sequence) - 1, sequence


# Example usage and test cases
if __name__ == "__main__":
    target_number = 96234
    min_operations, operations_sequence = primitive_calculator(target_number)
    print(min_operations)
    print(" ".join(map(str, operations_sequence)))

    # Additional test cases
    test_cases = [1, 5, 10, 15, 100, 200, 500, 1000, 10000]
    for test in test_cases:
        min_ops, ops_sequence = primitive_calculator(test)
        print(f"Minimum operations for {test}: {min_ops}")
        print(f"Sequence: {' '.join(map(str, ops_sequence))}\n")
