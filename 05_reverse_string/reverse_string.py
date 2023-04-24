def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    return phrase[::-1]

print(reverse_string("awesome"))
print(reverse_string("sauce"))


##ASK FOR WORD
while True:
    phrase=input("Enter a word: ")

     # Call the function
    result = reverse_string(phrase)

    # Print the result
    print(f"{result}")

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break