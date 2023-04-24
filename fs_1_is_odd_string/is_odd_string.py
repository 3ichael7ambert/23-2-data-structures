def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here

    # Create a mapping of letters to numbers
    letter_map = {letter: index + 1 for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}

    # Calculate the sum of character positions for each letter in the word
    total = sum(letter_map[letter.lower()] for letter in word)

    # Return True if the total is odd, False otherwise
    return total % 2 != 0

print("Should be True: ",is_odd_string('a'))
print("Should be True: ",is_odd_string('A'))
print("Should be False: ",is_odd_string('aaaa'))
print("Should be False: ",is_odd_string('AAaa'))
print("Should be True: ",is_odd_string('amazing'))