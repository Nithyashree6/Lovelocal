def shortestPalindrome(s):
    # Function to check if a substring is a palindrome
    def isPalindrome(sub):
        return sub == sub[::-1]

    # Find the index where the longest palindrome starts from the beginning
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if isPalindrome(s[:j + 1]):
            i = j + 1
            break

    # Construct the shortest palindrome by adding the reverse of the remaining characters to the start
    return s[i:][::-1] + s

# Test cases
print(shortestPalindrome("aacecaaa"))  
print(shortestPalindrome("abcd"))    
