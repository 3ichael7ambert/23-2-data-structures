def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

- a: friend #1, a tuple of (name, age, list-of-hobbies)
- b: same, for friend #2

Returns True if they have any hobbies in common, False is not.

    >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
    >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
    >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

    >>> friend_date(elmo, sauron)
    False

    >>> friend_date(sauron, gandalf)
    True
"""

# get list of hobbies for each friend
    a_hobbies = a[2]
    b_hobbies = b[2]

# check if there is any hobby in common
    for hobby in a_hobbies:
     if hobby in b_hobbies:
            return True

    return False

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])
friends= [elmo,sauron,gandalf]

print("Compare Elmo and Gandalf: ",friend_date(elmo, gandalf))
print("Compare Elmo and Sauron: ",friend_date(elmo, sauron))
print("Compare Sauron and Gandalf: ",friend_date(sauron, gandalf))
print()
