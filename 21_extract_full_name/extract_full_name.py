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

