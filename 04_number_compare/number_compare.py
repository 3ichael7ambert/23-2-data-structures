def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """

    if a==b:
        return 'Numbers are equal'
    if a>b:
        return "First number is greater"
    if a<b:
        return "Second number is greater"
    
print("Should be Equal: ", number_compare(4,4))
print("First is Bigger: ", number_compare(5,4))
print("Second is Bigger: ", number_compare(4,5))
print()

##ASK FOR NUMBERS
while True:
    a=input("Enter the first number: ")
    b=input("Enter the second number: ")

     # Call the function
    result = number_compare(a, b)

    # Print the result
    print(f"{result}")

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break