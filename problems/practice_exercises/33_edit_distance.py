def edit_distance(s1, s2):
    # Get the lengths of the strings
    len1, len2 = len(s1), len(s2)

    # Create a 2D DP table with dimensions (len1+1) x (len2+1)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Initialize the base cases for the first row and column
    for i in range(1, len1 + 1):
        dp[i][0] = i  # Deletion cost
    for j in range(1, len2 + 1):
        dp[0][j] = j  # Insertion cost

    # Fill the DP table using the given recurrence relation
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            # If characters are equal, no operation needed
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Choose the minimum of deletion, insertion, or substitution
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    # The final value in dp[len1][len2] is the edit distance
    return dp[len1][len2]


# Example usage and test cases
if __name__ == "__main__":
    # Example test case from the problem statement
    str1 = "short"
    str2 = "ports"
    print(
        f"Edit distance between '{str1}' and '{str2}': {edit_distance(str1, str2)}"
    )  # Expected Output: 3

    # Additional test cases
    test_cases = [
        ("editing", "distance"),
        ("kitten", "sitting"),
        ("flaw", "lawn"),
        ("intention", "execution"),
    ]
    for s1, s2 in test_cases:
        print(f"Edit distance between '{s1}' and '{s2}': {edit_distance(s1, s2)}")