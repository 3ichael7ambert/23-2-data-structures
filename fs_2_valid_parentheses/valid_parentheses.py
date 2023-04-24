def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """


    # initialize a counter for the parentheses
    count = 0

    # iterate through each character in the string
    for char in parens:
        # increment the count for an opening parenthesis
        if char == "(":
            count += 1
        # decrement the count for a closing parenthesis
        elif char == ")":
            count -= 1
        # if the count goes negative at any point, return False
        if count < 0:
            return False

    # if the count is 0 at the end, the parentheses are balanced
    return count == 0

print("Should be True: ",valid_parentheses("()"))
print("Should be True: ",valid_parentheses("()()"))
print("Should be True: ",valid_parentheses("(()())"))
print("Should be False: ",valid_parentheses(")()"))
print("Should be False: ",valid_parentheses("())"))
print("Should be False: ",valid_parentheses("((())"))
print("Should be False: ",valid_parentheses(")()("))