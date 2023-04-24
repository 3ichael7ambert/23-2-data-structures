def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    count = {}
    for char in phrase:
        if char.lower() in count:
            count[char.lower()] += 1
        else:
            count[char.lower()] = 1
    return count

print("Should be {'Y': 1, 'a': 1, 'y': 1}: ", multiple_letter_count('Yay'))
print("Should be {'y': 2, 'a': 1}: ", multiple_letter_count('yay'))
print()

##ASK FOR Word
while True:
    print("We are counting letters inside of words")
    phrase=input("Enter a word: ")

     # Call the function
    result = multiple_letter_count(phrase)

    # Print the result
    print(f"{result}")

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break