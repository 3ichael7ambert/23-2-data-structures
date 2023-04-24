def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    evenNums=1
    for num in nums:
        if num%2==0:
            evenNums=num*evenNums
    return evenNums
    
print("Should be 48: ",multiply_even_numbers([2, 3, 4, 5, 6]))
print("Should be 4: ",multiply_even_numbers([3, 4, 5]))
print("Should be 1: ",multiply_even_numbers([1, 3, 5]))

while True:
    lst = []
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num == 'done':
            break
        else:
            lst.append(int(num))
            print(lst)

    print(f"The Even Numbers of {lst} multiplied is:", multiply_even_numbers(lst))

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break