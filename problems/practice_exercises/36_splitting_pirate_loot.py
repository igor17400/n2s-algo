def can_split_loot(n, loot):
    total_sum = sum(loot)
    if total_sum % 3 != 0:
        return 0

    target_sum = total_sum // 3

    def backtrack(index, subset1, subset2, subset3):
        if index == n:
            return subset1 == subset2 == subset3 == target_sum

        if subset1 > target_sum or subset2 > target_sum or subset3 > target_sum:
            return False

        return (
            backtrack(index + 1, subset1 + loot[index], subset2, subset3)
            or backtrack(index + 1, subset1, subset2 + loot[index], subset3)
            or backtrack(index + 1, subset1, subset2, subset3 + loot[index])
        )

    return 1 if backtrack(0, 0, 0, 0) else 0


def test_splitting_pirate_loot():
    print("Testing can_split_loot function:")

    # Test case 1
    result = can_split_loot(4, [3, 3, 3, 3])
    print(f"Test 1 (Sample case): {'Passed' if result == 0 else 'Failed'}")

    # Test case 2
    result = can_split_loot(1, [30])
    print(f"Test 3 (Single item): {'Passed' if result == 0 else 'Failed'}")

    # Test case 4
    result = can_split_loot(13, [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25])
    print(f"Test 4 (Large equal sums): {'Passed' if result == 1 else 'Failed'}")


if __name__ == "__main__":
    test_splitting_pirate_loot()
