# 1- Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(num_list):
    for x in range(0, len(num_list), 1):
        if num_list[x] > 0:
            num_list[x] = "big"
    return num_list

print(biggie_size([-1, 3, 5, -5]))

# 2- Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(num_list):
    count = 0
    for x in range(0, len(num_list), 1):
        if num_list[x] > 0:
            count += 1
    num_list[len(num_list)-1] = count
    return num_list

print(count_positives([-1,1,1,1]))

# 3- Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(num_list):
    sumTotal = 0
    for x in range(0, len(num_list), 1):
        sumTotal += num_list[x]
    return sumTotal

print(sum_total([1,2,3,4]))


# 4- Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(num_list):
    sumTotal = 0
    for x in range(0, len(num_list), 1):
        sumTotal += num_list[x]
    return sumTotal/len(num_list)

print(average([1,2,3,4]))

# 5- Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(num_list):
    return len(num_list)

print(average([1,2,3,4]))
print(length([]))

# 6- Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(num_list):
    minimum = num_list[0]
    if len(num_list) > 0:
        for x in range(1, len(num_list), 1):
            if (num_list[x] < minimum ):
                minimum = num_list[x]      
        return minimum
    else:
        return False

print(minimum([37,2,1,-9]))

# 7- Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(num_list):
    maximum = num_list[0]
    if len(num_list) > 0:
        for x in range(1, len(num_list), 1):
            if (num_list[x] > maximum ):
                maximum = num_list[x]
        return maximum
    else:
        return False

print(maximum([37,2,1,-9]))


# 8- Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(num_list):
    sumTotal = 0
    minimum = num_list[0]
    maximum = num_list[0]
    thisdict = {}
    for x in range (0, len(num_list), 1):
        sumTotal += num_list[x]
        if (num_list[x] > maximum ):
            maximum = num_list[x]
        if (num_list[x] < minimum ):
            minimum = num_list[x]
    thisdict["sumTotal"] = sumTotal
    thisdict["average"] = sumTotal/len(num_list)
    thisdict["minimum"] = minimum
    thisdict["maximum"] = maximum
    thisdict["length"] = len(num_list)
    return thisdict

print(ultimate_analysis([37,2,1,-9]))

# 9- Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(num_list):
    temp = 0
    for x, y in zip(range(0, int(len(num_list)/2), 1), range(len(num_list)-1, 0, -1)):
            temp = num_list[x]
            num_list[x] = num_list[y]
            num_list[y] = temp
    return num_list

print(reverse_list([37,2,1,-9]))