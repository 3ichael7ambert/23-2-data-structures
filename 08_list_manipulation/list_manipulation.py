def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """


    if command == 'add':
        if location == 'beginning':
            lst.insert(0, value)
        elif location == 'end':
            lst.append(value)
    elif command == 'remove':
        if location == 'beginning':
            return lst.pop(0)
        elif location == 'end':
            return lst.pop()
    return None


lst=[1, 2, 3]
print("ORIGINAL LIST: ",lst)
list_manipulation(lst, 'remove', 'end')
print(lst)
list_manipulation(lst, 'remove', 'beginning')
print(lst)
list_manipulation(lst, 'add', 'beginning', 20)
print(lst)
list_manipulation(lst, 'add', 'end', 30)
print(lst)

list_manipulation(lst, 'foo', 'end') 
print(lst)
list_manipulation(lst, 'add', 'dunno') 
print(lst)



##ASK FOR Word
while True:
    print("Now you can edit this list")
    command = input("Are we adding or removing (add/remove): ")
    while command not in ['add', 'remove']:
        command = input("Are we adding or removing (add/remove): ")
    if command == 'add':
        value = int(input("What value are we adding: "))
    else:
        value = None
    location = input(f"{command} to beginning or end? (beginning/end): ")
    while location not in ['beginning', 'end']:
        location = input(f"{command} to beginning or end? (beginning/end): ")
    result = list_manipulation(lst, command, location, value)
    print(f"UPDATED LIST: {lst}")
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break