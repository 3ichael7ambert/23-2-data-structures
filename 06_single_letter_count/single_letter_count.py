def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    count=0
    for char in word:
         if char.lower() == letter.lower():
            count += 1
    return count

print("Should be 1 h in Hello: ", single_letter_count('Hello World', 'h'))
print("Should be no z in Hellow World: ", single_letter_count('Hello World', 'z'))
print("Should be 3 l in Hello World: ", single_letter_count("Hello World", 'l'))
print()

##ASK FOR Letters in Word
while True:
    print("We are counting letters inside of words")
    word=input("First, Enter a word: ")
    letter=input("Secondly, Enter a letter: ")

     # Call the function
    result = single_letter_count(word, letter)

    # Print the result
    print(f"{result}")

    # Ask the user if they want to continue
    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() == 'n':
        break