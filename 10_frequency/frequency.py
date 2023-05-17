def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    count = 0
    for idx in lst:
        if idx == search_term:
            count = count + 1
    return count

print("Should be 3: ", frequency([1, 4, 3, 4, 4], 4))
print("Should be 0: ", frequency([1, 4, 3], 7))

lst=[]
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num == 'done':
        break
    else:
        lst.append(int(num))
        print(lst)
    lstInput = int(input("Enter a list: "))###
    search_term = int(input("Enter the number to find frequency of: "))
    freq = frequency(lstInput, search_term)###
    print(f"The frequency of {search_term} in the list is: {freq}")

# Ask the user if they want to continue
choice = input("Do you want to continue? (y/n): ")
if choice.lower() == 'n':
    break
