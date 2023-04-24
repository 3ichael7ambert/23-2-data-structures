def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    # Convert both numbers to strings
    str1 = str(num1)
    str2 = str(num2)
    
    # If the lengths are not equal, the frequencies cannot be the same
    if len(str1) != len(str2):
        return False
    
    # Create dictionaries to store the frequency of each digit for both numbers
    freq1 = {}
    freq2 = {}
    
    # Loop through each digit in both numbers and update the corresponding frequency
    for digit in str1:
        freq1[digit] = freq1.get(digit, 0) + 1
    for digit in str2:
        freq2[digit] = freq2.get(digit, 0) + 1
    
    # Compare the frequencies of each digit for both numbers
    for digit in freq1:
        if freq1[digit] != freq2.get(digit, 0):
            return False
    
    return True

print("Should be True: ",same_frequency(551122, 221515))
print("Should be False: ",same_frequency(321142, 3212215))
print("Should be True: ",same_frequency(1212, 2211))