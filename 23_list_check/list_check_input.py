def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for idx in lst:
        if not isinstance(idx, list):
            return False
    return True


print("Should be true: ", list_check([[1], [2, 3]]))
print("Should be false: ", list_check([[1], "nope"]))
print()

newList = []
while True:
    idx = input("Enter a list (or 'done' to stop): ")
    if idx == "done":
        break
    else:
        try:
            lst = eval(idx)
            if not isinstance(lst, list):
                print("Error: Input must be a list!")
            else:
                newList.append(lst)
                print(newList)
        except:
            print("Error: Invalid input!")

print("The lists you entered are:", newList)
print("The indices are only nested lists: ", list_check(newList))

# Ask the user if they want to continue
while True:
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break
