def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    total = 0
    for num in nums:
        if isinstance(num, float):
            total += num
    return total


numbers = []
while True:
    num = input("Enter a number (or 'done' to stop): ")
    if num == "done":
        break
    try:
        num = float(num)
    except ValueError:
        print("Invalid input, please enter a number or 'done'")
    else:
        numbers.append(num)
        print(numbers)

print("The numbers you entered are:", numbers)
print("The sum of the floating point numbers is:", sum_floats(numbers))

# Ask the user if they want to continue
while True:
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break
