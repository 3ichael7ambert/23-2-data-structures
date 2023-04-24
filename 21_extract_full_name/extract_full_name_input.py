def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    names = []
    for person in people:
        full_name = person['first'] + ' ' + person['last']
        names.append(full_name)
    return names

names = [    {'first': 'Ada', 'last': 'Lovelace'},    {'first': 'Grace', 'last': 'Hopper'},]

full_names = extract_full_names(names)
print(full_names)
print()

while True:
    print("Now, Let's add your name to the 'dictionary'!")
    first = input("What is your first name?: ")
    last = input("What is your last name?: ")
    
    # create a new dictionary for the user's name
    person = {'first': first, 'last': last}
    full_name = person['first'] + ' ' + person['last']
    names.append(person)
    full_names = extract_full_names(names)
    print(full_names)
    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break
