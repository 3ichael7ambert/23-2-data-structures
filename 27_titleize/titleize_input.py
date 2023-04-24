def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    newPhrase = ""
    for word in phrase.split(' '):
        newPhrase += word.capitalize() + " "
    return newPhrase

print("Should be 'This Is Awesome': ",titleize('this is awesome'))
print("Should be 'Only Capitalize First': ",titleize('oNLy cAPITALIZe fIRSt'))
print()

while True:
    # Get input from the user
    user_input = input("Enter a sentence: ")

    # Call the titleize function on the user input
    titleized_sentence = titleize(user_input)

    # Print the titleized sentence
    print(titleized_sentence)

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break