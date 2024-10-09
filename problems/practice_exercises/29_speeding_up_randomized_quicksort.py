from random import randint


def partition3(array, left, right):
    # Three-way partition: arr[left..m1-1] < pivot, arr[m1..m2] == pivot, arr[m2+1..right] > pivot
    pivot = array[left]
    m1 = left  # The initial index for elements less than the pivot
    m2 = right  # The initial index for elements greater than the pivot

    i = left  # Current index
    while i <= m2:
        if array[i] < pivot:
            array[i], array[m1] = array[m1], array[i]  # Swap with m1 and move m1
            m1 += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[m2] = array[m2], array[i]  # Swap with m2 and move m2
            m2 -= 1
        else:
            i += 1  # If element is equal to pivot, move i to the right

    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)  # Randomly select a pivot
    array[left], array[k] = array[k], array[left]  # Move pivot to start of the array
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)

# Static Examples for Testing

# Example 1: Array with duplicates
elements = [2, 3, 9, 2, 9]
print(f"Original Array: {elements}")
randomized_quick_sort(elements, 0, len(elements) - 1)
print(f"Sorted Array: {elements}\n")

# Example 2: Array with distinct elements
elements = [5, 3, 8, 6, 2, 1]
print(f"Original Array: {elements}")
randomized_quick_sort(elements, 0, len(elements) - 1)
print(f"Sorted Array: {elements}\n")

# Example 3: Already sorted array
elements = [1, 2, 3, 4, 5, 6]
print(f"Original Array: {elements}")
randomized_quick_sort(elements, 0, len(elements) - 1)
print(f"Sorted Array: {elements}\n")

# Example 4: Reverse sorted array
elements = [6, 5, 4, 3, 2, 1]
print(f"Original Array: {elements}")
randomized_quick_sort(elements, 0, len(elements) - 1)
print(f"Sorted Array: {elements}\n")

# Example 5: Array with all elements the same
elements = [7, 7, 7, 7, 7]
print(f"Original Array: {elements}")
randomized_quick_sort(elements, 0, len(elements) - 1)
print(f"Sorted Array: {elements}\n")

# Example 6: Array with one element
elements = [42]
print(f"Original Array: {elements}")
randomized_quick_sort(elements, 0, len(elements) - 1)
print(f"Sorted Array: {elements}\n")

# Example 7: Array with negative numbers
elements = [-1, -5, 3, 6, -2, 4]
print(f"Original Array: {elements}")
randomized_quick_sort(elements, 0, len(elements) - 1)
print(f"Sorted Array: {elements}\n")

# Example 8: Mixed positive and negative numbers
elements = [10, -1, 0, 5, -10, 3]
print(f"Original Array: {elements}")
randomized_quick_sort(elements, 0, len(elements) - 1)
print(f"Sorted Array: {elements}\n")
