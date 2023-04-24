def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if len(lst) == 0:
        return None
    else:
        return lst[len(lst)-1] 
        ## return lst[-1]  also works

print("Should be 5: ", last_element([1, 2, 3, 4, 5]))
print("Should be 3: ", last_element([1, 2, 3, 4, 4,9,4,3]))
print()



lst=[]
# Loop until the user enters "done"
while True:
    # Ask for user input
    user_input = input("Enter a number or string (or 'done' to stop): ")
    
    # If user enters "done", break out of the loop
    if user_input == 'done':
        break
    
    # Otherwise, append the user input to the list
    lst.append(user_input)

# Call the last_element function with the list
result = last_element(lst)

# Print the result
print(f"The last element is: {result}")