import math


def func(A):
    # Length of the array to be sorted
    n = len(A)

    # Set to stop when the length becomes 1 through recursive calls
    if (n == 1):
        return A

    # Index of the middle element in array A
    # Include the smaller side if the length is odd
    m = math.floor(n / 2)
    # Left array
    L = func(A[0:m])
    # Right array
    R = func(A[m:n])

    # Empty array to store the result
    B = []
    # Index being considered when examining L and R
    i = j = 0

    # Repeat until the considered index is equal to the length of both left and right arrays
    while (i < len(L) or j < len(R)):
        # If i has examined elements and there are still unexamined elements with j
        if (i == len(L) and j < len(R)):
            # Append the sorted element that j is examining to B
            B.append(R[j])
            # Move to the next element with j
            j = j + 1
        # If j has examined elements and there are still unexamined elements with i
        elif (j == len(R) and i < len(L)):
            # Append the sorted element that i is examining to B
            B.append(L[i])
            # Move to the next element with i
            i = i + 1
        # If the element being examined by i is less than or equal to the element being examined by j
        elif (L[i] <= R[j]):
            # Put the element being examined by i into B
            B.append(L[i])
            # Move to the next element with i
            i = i + 1
        # If the element being examined by j is smaller than the element being examined by i
        else:
            # Put the element being examined by j into B
            B.append(R[j])
            # Move to the next element with j
            j = j + 1
    # Display B at the end of each recursive phase
    print(B)
    # Return B at the end of each recursive phase
    return B


lst = [2, 9, 5, 3, 7, 0, 1, 4]
func(lst)
