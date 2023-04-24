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

print("Compare Elmo and Gandalf",friend_date(elmo, gandalf))
print("Compare Elmo and Sauron",friend_date(elmo, sauron))
print("Compare Sauron and Gandalf",friend_date(sauron, gandalf))
print()

# prompt user to select two friends to compare
while True:
    friends_names = [friend[0] for friend in friends]
    print(friends_names)
    friend1 = input("Enter the name of the first friend: ")
    friend2 = input("Enter the name of the second friend: ")
    
    # find the tuples that match the input names
    friend1_tuple = None
    friend2_tuple = None
    for friend in friends:
        if friend[0] == friend1:
            friend1_tuple = friend
        elif friend[0] == friend2:
            friend2_tuple = friend
    
    # check if both friends were found
    if friend1_tuple is None or friend2_tuple is None:
        print("Invalid input. Please enter the names of two existing friends.")
        continue
    
    # compare the friends and print the result
    if friend_date(friend1_tuple, friend2_tuple):
        print(f"{friend1} and {friend2} have at least one hobby in common!")
    else:
        print(f"{friend1} and {friend2} don't seem to have any hobbies in common.")
    
    # ask if the user wants to compare more friends
    again = input("Compare more friends? (y/n)")
    if again.lower() != 'y':
        break

# prompt user to add a new friend to the list
while True:
    name = input("Enter the name of your new friend: ")
    age = input("Enter their age: ")
    hobbies = input("Enter their hobbies, separated by commas: ").split(',')
    new_friend = (name, int(age), [hobby.strip() for hobby in hobbies])
    friends.append(new_friend)
    friends_names = [friend[0] for friend in friends]
    print(friends_names)
    # ask if the user wants to add another friend
    again = input("Add another friend? (y/n): ")
    if again.lower() != 'y':
        break

# print updated list of friends
print("Here are your friends now:")
for friend in friends:
    print(friend[0])

# prompt user to compare two friends again
while True:
        # prompt user to compare two friends again
    print("Enter the names of two friends to compare their hobbies, or enter 'quit' to exit:")
    friend1 = input("Enter the name of the first friend: ")
    if friend1 == 'quit':
        break
    friend2 = input("Enter the name of the second friend: ")
    if friend2 == 'quit':
        break

    # search for the friends in the list
    found_friend1 = False
    found_friend2 = False
    for friend in friends:
        if friend[0] == friend1:
            friend1_info = friend
            found_friend1 = True
        if friend[0] == friend2:
            friend2_info = friend
            found_friend2 = True

    # compare the hobbies of the two friends
    if found_friend1 and found_friend2:
        if friend_date(friend1_info, friend2_info):
            print(f"{friend1_info[0]} and {friend2_info[0]} have at least one hobby in common!")
        else:
            print(f"{friend1_info[0]} and {friend2_info[0]} don't have any hobbies in common.")
    else:
        print("Sorry, I couldn't find one or both of those friends. Please try again.")
while True:
    print("Here are your friends now:")
    for friend in friends:
     print(friend[0])
     print()

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break
