def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # Create an empty set to store the seen numbers
    seen = set()

    # Loop through the numbers in the list
    for num in nums:

        # Check if the difference between the goal and current number is in the seen set
        if goal - num in seen:

            # If it is, return the pair as a tuple
            return (goal - num, num)

        # Otherwise, add the current number to the seen set
        seen.add(num)

    # If no pairs were found, return an empty tuple
    return ()

print("Should be (2, 2): ",sum_pairs([1, 2, 2, 10], 4))
print("Should be (4, 2): ",sum_pairs([4, 2, 10, 5, 1], 6))
print("Should be (4, 3): ",sum_pairs([5, 1, 4, 8, 3, 2], 7))
print("Should be (): ",sum_pairs([11, 20, 4, 2, 1, 5], 100))
print("Should be (5, 3): ",sum_pairs([1, 5, 6, 3, 7], 8))
print("Should be (5, 0): ",sum_pairs([-2, 5, 10, -3, 0, 1], 5))
print("Should be (): ",sum_pairs([], 10))
