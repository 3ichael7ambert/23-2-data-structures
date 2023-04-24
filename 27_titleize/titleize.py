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