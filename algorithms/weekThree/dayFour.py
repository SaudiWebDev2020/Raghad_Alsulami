# Is Palindrome
# --------------------------------------------------------------------------------
# Strings like "Able was I, ere I saw Elba" or "Madam, I'm Adam" could be considered palindromes, 
# because (if we ignore spaces, punctuation and capitalization) the letters are the same from front and back.
# Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", 
# return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.

def isPalindrome(string):
    for i in range(len(string)): 
        if string[i] != string[len(string)-i-1]:
            return False
    return True

print(isPalindrome("a x a"))
print(isPalindrome("racecar"))
print(isPalindrome("Dud"))
print(isPalindrome("oho!"))

# Longest Palindrome
# --------------------------------------------------------------------------------
# For this challenge, we will look not only at the entire string, but also substrings within it. 
# For a string, return the longest palindromic substring. Given "what up, dada?", return "dad".
# Given "not much", return "n". Include spaces as well (i.e. be strict, as in the “Is Palindrome” challenge): 
# given "My favorite racecar erupted!", return "e racecar e".

def longestPalindrome(string):
    longest = ''
    for i in range(len(string)):
        for j in range(len(string),i,-1):
            if string[i:j] == string[i:j][::-1]:
                if len(longest) < len(string[i:j]):
                    longest = string[i:j]
    return longest        


print(longestPalindrome('what up, dada?'))
print(longestPalindrome('not much'))
print(longestPalindrome("My favorite racecar erupted!"))