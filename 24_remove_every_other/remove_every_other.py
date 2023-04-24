def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    newLst=[]
    alt=1
    for idx in lst:
        if alt==1:
            newLst.append(idx)
            alt=0
        elif alt==0:
            alt=1
    return newLst

lst = [1, 2, 3, 4, 5]
print("Returned List (not mutated):", remove_every_other(lst))
print("Original List: ",lst)