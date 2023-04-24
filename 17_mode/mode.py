def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = 0
    mode_num = None
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            mode_num = num

    return mode_num
print("Should be 1: ",mode([1, 2, 1]))
print("Should be 2: ",mode([2, 2, 3, 3, 2]))
print()

while True:
    print("Your turn to create a list and find the Mode")
    lst = []
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num == 'done':
            break
        else:
            lst.append(int(num))
            print(lst)

    print(f"The Mode of {lst}, (Most common numbers) is: ", mode(lst))

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break