def parse_input_string(input_str):
    """Parse an input string into its respective Python data type."""
    input_str = input_str.strip()  # remove whitespace from the beginning and end
    if input_str.lower() == "false":
        return False
    elif input_str.lower() == "true":
        return True
    elif input_str.lower() == "none":
        return None
    elif input_str.isdigit():
        return int(input_str)
    elif input_str.startswith("[") and input_str.endswith("]"):
        # parse a list
        return eval(input_str)
    elif input_str.startswith("(") and input_str.endswith(")"):
        # parse a tuple
        return eval(input_str)
    elif input_str.startswith("{") and input_str.endswith("}"):
        # parse a dictionary
        return eval(input_str)
    else:
        # assume it's a string
        return input_str


def compact(lst):
    """Return a copy of lst with non-true elements removed.

    >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    [1, 2, 'All done']
    """

    new_lst = []
    for item in lst:
        if item not in (False, None, '', [], ()):
            new_lst.append(parse_input_string(item))
    return new_lst


while True:
    print("Now you can create a list, when finished we will remove the empty units")
    lst = []
    while True:
        tdx = input("Enter a number, string, list, tuple, dictionary (or 'done' to finish): ")
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
