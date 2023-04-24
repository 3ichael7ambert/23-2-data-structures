def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newPhrase=""
    for char in phrase:
        if char.lower()==to_swap.lower():
            newPhrase+=char.swapcase()
        else:
            newPhrase+=char
    return newPhrase

print("'Aaaah', 'a', should be 'aAAAhhh'",flip_case('Aaaahhh', 'a'))
print("'Aaaah', 'A', should be 'aAAAhhh'",flip_case('Aaaahhh', 'A'))
print("'Aaaah', 'a', should be 'AaaaHHH'",flip_case('Aaaahhh', 'h'))
print()

#Enter your own word
while True:
        print("Now you get to choose a word to caseswap")
        phrase = input("Enter a word: ")
        to_swap = input("Choose a letter to case swap: ")
        print(f"Your word {phrase} with a caseswap for {to_swap} is: ", flip_case(phrase, to_swap))
        print()

        # Ask the user if they want to continue
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == 'n':
             break