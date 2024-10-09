def longest_common_subsequence(seq1, seq2):
    # Get the lengths of both sequences
    len1, len2 = len(seq1), len(seq2)

    # Create a DP table with dimensions (len1+1) x (len2+1) initialized to 0
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Fill the DP table using the given recurrence relation
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
                # If the elements are equal, extend the LCS by 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Take the maximum LCS by ignoring one element from either seq1 or seq2
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The value in dp[len1][len2] is the length of the longest common subsequence
    return dp[len1][len2]


# Example usage and test cases
if __name__ == "__main__":
    # # Example test case from the problem statement
    # seq1 = [7, 2, 9, 3, 1]
    # seq2 = [2, 8, 1, 3, 9, 7]
    # print(
    #     f"Length of LCS: {longest_common_subsequence(seq1, seq2)}"
    # )  # Expected Output: 3

    # # Additional test cases
    # test_cases = [
    #     ([1, 2, 3], [2, 3, 4]),  # Expected Output: 2
    #     ([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7]),  # Expected Output: 4
    #     ([1, 2, 3, 4], [1, 3, 5, 6]),  # Expected Output: 2
    #     ([5, 6, 7, 8], [7, 6, 8, 5]),  # Expected Output: 2
    # ]
    # for s1, s2 in test_cases:
    #     print(
    #         f"Length of LCS between {s1} and {s2}: {longest_common_subsequence(s1, s2)}"
    #     )

    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(longest_common_subsequence(a, b))
