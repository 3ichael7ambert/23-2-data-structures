def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    freq = {}

    for char in phrase.lower():
        if char in vowels:
            freq[char] = freq.get(char, 0) + 1

    return freq

print("Should return {'i': 1, 'o': 2}: ",vowel_count('rithm school'))
print("Should return {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}: ",vowel_count('HOW ARE YOU? i am great!') )