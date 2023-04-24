def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    newPhrase=""
    currentLetter=1
    for char in phrase:
        if currentLetter==1:
            newPhrase+=char.upper()
            currentLetter+=1
        else:
            newPhrase+=char
    return newPhrase

print("Should be 'Python': ",capitalize('python'))
print("Should be 'Only first word': ",capitalize('only first word'))
print()

#Enter your own word
while True:
        print("Now you get to choose a sentence to capitalize")
        phrase = input("Enter a sentence: ")
        print(f"Your new sentence is: ", capitalize(phrase))
        print()

        # Ask the user if they want to continue
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == 'n':
             break