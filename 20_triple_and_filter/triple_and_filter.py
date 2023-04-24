def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    newLst=[]
    for num in nums:
        if num%4==0:
            newLst+=[num*3]
    return newLst

print("Should be [12]:",triple_and_filter([1, 2, 3, 4]))
print("Should be [24, 36]:",triple_and_filter([6, 8, 10, 12]))
print("Should be []:",triple_and_filter([1, 2]))
print()

while True:
    print("Your turn to create a list")
    lst = []
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num == 'done':
            break
        else:
            lst.append(int(num))
            print(lst)

    print(f"The list of {lst}, with divisible by 4 but multiplied by 3: ", triple_and_filter(lst))

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break