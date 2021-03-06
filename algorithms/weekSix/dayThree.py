# Binary String Expansion
# ---------------------------------------------------------------------------------
# You will be given a string containing characters ‘0’, ‘1’, and ‘?’. For every ‘?’, 
# either ‘0’ or ‘1’ characters can be substituted. Write a recursive function that returns 
# an array of all valid strings that have ‘?’ characters expanded into ‘0’ or ‘1’.
# Ex.: binStrExpand("1?0?") should return ["1000","1001","1100","1101"]. For this challenge, 
# you can use string functions such as slice(), etc., but be frugal with their use, as they are expensive.

def binStrExpand(string, index = 0, temp_str='', possibilities = []):
    for index, character in enumerate(string): 
        if character =='?':
            binStrExpand(string[index+1:], index, temp_str, possibilities)
            for num in range(0,2):
                temp_str += str(num)
        else: 
            temp_str += character
    possibilities.append(temp_str)
    return possibilities

print(binStrExpand('000?'))
