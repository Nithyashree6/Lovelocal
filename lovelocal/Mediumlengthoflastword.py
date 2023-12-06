def length_of_last_word(s):
    # Trim any trailing spaces
    s = s.rstrip()
    
    # Initialize a variable to store the length of the last word
    length = 0
    
    # Traverse the string from the end
    for char in reversed(s):
        # Check for the first space encountered from the end
        if char == ' ':
            break
        # Increment the length of the last word
        length += 1
    
    return length

# Test cases
print(length_of_last_word("Hello World"))  
print(length_of_last_word("   fly me   to   the moon  ")) 
print(length_of_last_word("luffy is still joyboy"))  
