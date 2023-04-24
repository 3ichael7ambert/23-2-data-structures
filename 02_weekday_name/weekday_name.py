def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if day_of_week==1:
        return 'Sunday'
    elif day_of_week==2:
        return 'Monday'
    elif day_of_week==3:
        return 'Tuesday'
    elif day_of_week==4:
        return 'Wednesday'
    elif day_of_week==5:
        return 'Thursday'
    elif day_of_week==6:
        return 'Friday'
    elif day_of_week==7:
        return 'Saturday'
    else:
        return None
    

print("Should be Sunday: ",weekday_name(1))
print("Should be Tuesday: ",weekday_name(3))
print("Should be Thursday: ",weekday_name(5))
print()


while True:
    # Ask for user input
    a = int(input("Enter Day number 1 to 7: "))

    # Call the function
    result = weekday_name(a)

    # Print the result
    print(f"The product is: {result}")

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break