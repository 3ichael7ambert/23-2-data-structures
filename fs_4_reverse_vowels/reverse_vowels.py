def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """



    # Convert the string into a list for easy manipulation
    s_list = list(s)

    # Create a set of vowels
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    # Initialize two pointers, one at the beginning and one at the end of the string
    left, right = 0, len(s_list) - 1

    # Iterate until the two pointers meet
    while left < right:

        # If the left pointer is not pointing at a vowel, move it to the right
        if s_list[left] not in vowels:
            left += 1

        # If the right pointer is not pointing at a vowel, move it to the left
        elif s_list[right] not in vowels:
            right -= 1

        # If both pointers are pointing at vowels, swap them and move the pointers inward
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    # Convert the list back into a string and return it
    return ''.join(s_list)

print("Should be 'Holle!': ",reverse_vowels("Hello!"))
print("Should be 'Temotaos': ",reverse_vowels("Tomatoes"))
print("Should be 'RivArsI Vewols en e Streng': ",reverse_vowels("Reverse Vowels In A String"))
print("Should be 'uoiea': ",reverse_vowels("aeiou"))
print("Should be 'why try, shy fly?': ",reverse_vowels("why try, shy fly?"))