# Arrs2Map
# ----------------------------------------------------------------------------------------------------------------
# Given two arrays, create an associative array (map) containing keys of the first, and values of the
# second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc":
# 42, 3: "wassup", "yo": true}.

list1 = ["abc", 3, "yo"]
list2 = [42, "wassup", True]

def arrs2Map(list1, list2):
    obj = {}
    for i in range(0, len(list1), 1):
        obj[list1[i]] = list2[i]
    return obj

print(arrs2Map(list1, list2))

# InvertHash
# ----------------------------------------------------------------------------------------------------------------
# Create invertHash(assocArr) that converts a hash’s keys to values and values to corresponding keys.
# Example: given {"name": "Zaphod"; "numHeads": 2}, return {"Zaphod": "name"; 2:
# "numHeads"}. You will need to learn and use a Python for ... in here!

obj = {"name": "Zaphod", "numHeads": 2}
def invertHash(obj):
    pass
    

# print(invertHash(obj))

# ReverseString
# ----------------------------------------------------------------------------------------------------------------
# Implement a function reverseString(str) that, given a string, will return the string of the same length but
# with characters reversed. Example: given "creature", return "erutaerc". Do not use the built-in
# reverse() function!

string = "creature"

def reverseString(string):
    newStr = ""
    for i in string:
        newStr = i + newStr
    return newStr

print(reverseString(string))