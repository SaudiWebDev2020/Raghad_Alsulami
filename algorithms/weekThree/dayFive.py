# Book Index
# ------------------------------------------------------------------------
# Write a function that given a sorted array of page numbers, return a string representing a book index.
# Combine consecutive pages to create ranges. Given [1, 3, 4, 5, 7, 8, 10], return the string "1, 3-5, 7-8, 10".
arr = [1, 3, 4, 5, 7, 8, 10]
def bookIndex(arr): 
    string =''
    cons_str=''
    for i in range(len(arr)): 
        if i == len(arr)-1:
            string += str(arr[i])
        elif arr[i+1] != arr[i]+1:
            string += str(arr[i]) +', '
        else:
            cons_str += str(arr[i]) +', '
    print(cons_str)
    return string

print(bookIndex(arr))

# Common Suffix
# ------------------------------------------------------------------------
# When given an array of words, returns the largest suffix (word-end) that is common between all words. 
# For example, for input ["ovation", "notation", "action"], return "tion". Given ["nice", "ice", "sic"], return "".

arr = ["ovation", "notation", "action"]
res = '' 
prefix = arr[len(arr)-1] 
for string in arr[len(arr):]: 
    while string[:len(prefix)] != prefix and prefix: 
        prefix = prefix[:len(prefix)-1] 
    if not prefix: 
        break
res = prefix 

print("Resultant prefix", str(res)) 
