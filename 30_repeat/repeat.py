def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    if not isinstance(num, int) or num < 0:
        return None
    else:
        return phrase * num

print("Should be '***':",repeat('*', 3))
print("Should be 'abcabc'':",repeat('abc', 2))
print("Should be '':",repeat('abc', 0))