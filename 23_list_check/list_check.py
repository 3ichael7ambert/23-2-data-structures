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
        

print("Should be true: ",list_check([[1], [2, 3]]))
print("Should be false: ",list_check([[1], "nope"]))