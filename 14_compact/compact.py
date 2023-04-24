def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    newLst=[]
    for idx in lst:
        if not idx in (False, None, '', [],()):
            newLst.append(idx)
    return newLst

print("[0, 1, 2, '', [], False, (), None, 'All done'] should become [1, 2, 'All done']:  ",compact([0, 1, 2, '', [], False, (), None, 'All done']))
print()

while True:
    print("Now you can create a list, when finished we will remove the empty units")
    lst = []
    while True:
        tdx = input("Enter a number, string, list (or 'done' to finish): ")
        if tdx == 'done':
            break
        else:
            lst.append(tdx)
            print(lst)

    print(f"The Removed Empty indexes of {lst} is:", compact(lst))

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break