def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """

    return a*b
print(product(1,4),"should be 5")
print(product(4,3),"should be 7")
print("")


while True:
    # Ask for user input
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Call the function
    result = product(a, b)

    # Print the result
    print(f"The product is: {result}")

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break