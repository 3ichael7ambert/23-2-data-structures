def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    newLst=[]
    for idx1 in l1:
        for idx2 in l2:
            if idx1==idx2:
                newLst.append(idx1)
    return newLst

print("Should be [2, 3]: ",intersection([1, 2, 3], [2, 3, 4]))
print("Should be [1, 2, 3]: ",intersection([1, 2, 3], [1, 2, 3, 4]))
print("Should be [3]: ",intersection([1, 2, 3], [3, 4]))
print("Should be []: ",intersection([1, 2, 3], [4, 5, 6]))
print()


while True:
    print("Now you make two lists to find their intersections")
    l1 = []
    l2 = []
    while True:
        idx = input("Enter a number for the first list (or 'done' to finish): ")
        if idx == 'done':
            break
        else:
            l1.append(int(idx))
            print(l1)
    while True:
        idx = input("Enter a number for the second list (or 'done' to finish): ")
        if idx == 'done':
            break
        else:
            l2.append(int(idx))
            print(l2)

    print(f"The intersection of {l1} and {l2} is:", intersection(l1, l2))

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break