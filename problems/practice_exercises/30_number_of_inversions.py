def inversions_optimized(arr):
    # Helper function to perform merge sort and count inversions
    def merge_sort(arr, temp_arr, left, right):
        if left >= right:
            return 0

        # Calculate mid point
        mid = (left + right) // 2
        inv_count = 0

        # Count inversions in the left half
        inv_count += merge_sort(arr, temp_arr, left, mid)

        # Count inversions in the right half
        inv_count += merge_sort(arr, temp_arr, mid + 1, right)

        # Count split inversions
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

        return inv_count

    # Helper function to merge two halves and count inversions
    def merge_and_count(arr, temp_arr, left, mid, right):
        i = left  # Left subarray index
        j = mid + 1  # Right subarray index
        k = left  # Temporary array index
        inv_count = 0

        # Traverse both halves and count split inversions
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (
                    mid - i + 1
                )  # Elements in left half are greater than arr[j]
                j += 1
            k += 1

        # Copy remaining elements of the left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy remaining elements of the right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy the sorted subarray into the original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    # Main function body
    temp_arr = arr[:]
    return merge_sort(arr, temp_arr, 0, len(arr) - 1)


# Static Examples for Testing

# Example 1: A small array with a few inversions
elements = [2, 3, 9, 2, 9]
print(f"Array: {elements}")
print(f"Number of Inversions: {inversions_optimized(elements)}\n")  # Expected output: 2

# Example 2: Array with all elements sorted in descending order
elements = [5, 4, 3, 2, 1]
print(f"Array: {elements}")
print(
    f"Number of Inversions: {inversions_optimized(elements)}\n"
)  # Expected output: 10

# Example 3: Array with no inversions (already sorted)
elements = [1, 2, 3, 4, 5]
print(f"Array: {elements}")
print(f"Number of Inversions: {inversions_optimized(elements)}\n")  # Expected output: 0

# Example 4: Array with duplicates
elements = [3, 3, 3, 3, 3]
print(f"Array: {elements}")
print(f"Number of Inversions: {inversions_optimized(elements)}\n")  # Expected output: 0

# Example 5: Array with alternating high and low values
elements = [1, 3, 2, 4, 3, 5]
print(f"Array: {elements}")
print(f"Number of Inversions: {inversions_optimized(elements)}\n")  # Expected output: 2

# Example 6: Large array with random values
elements = [12, 11, 13, 5, 6, 7]
print(f"Array: {elements}")
print(
    f"Number of Inversions: {inversions_optimized(elements)}\n"
)  # Expected output: 10

# Example 7: Single element array
elements = [1]
print(f"Array: {elements}")
print(f"Number of Inversions: {inversions_optimized(elements)}\n")  # Expected output: 0

# Example 8: Array with only two elements and no inversions
elements = [1, 2]
print(f"Array: {elements}")
print(f"Number of Inversions: {inversions_optimized(elements)}\n")  # Expected output: 0

# Example 9: Array with only two elements and one inversion
elements = [2, 1]
print(f"Array: {elements}")
print(f"Number of Inversions: {inversions_optimized(elements)}\n")  # Expected output: 1

# Example 10: Large array with random values
elements = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Array: {elements}")
print(
    f"Number of Inversions: {inversions_optimized(elements)}\n"
)  # Expected output: 45
