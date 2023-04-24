def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    newPhrase=phrase[::-1]
    if newPhrase==phrase:
        return True
    else:
        return False
    
print("Should be True: ",is_palindrome('tacocat'))
print("Should be True: ",is_palindrome('noon'))
print("Should be False: ",is_palindrome('robert'))
print()

#ASK FOR Word
while True:
    print("Let us learn and check for palindromes")
    phrase=input("First, Enter a word: ")

     # Call the function
    result = is_palindrome(phrase)

    if result==True:
    # Print the result
        print(f"{phrase} is a palindrome")
    else:
        print(f"{phrase} is NOT a palindrome")
    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break
    

#ASK FOR Word
while True:
    print("Let us learn and check for palindromes")
    phrase=input("First, Enter a word: ")

     # Call the function
    result = is_palindrome(phrase)

    if result==True:
    # Print the result
        print(f"{phrase} is a palindrome")
    else:
        print(f"{phrase} is NOT a palindrome")
    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break
    
