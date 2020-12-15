import math
# Recursive Fibonacci
# ------------------------------------------------------------------------------------------------------------------------
# Write rFib(num). Recursively compute and return the numth Fibonacci value. As earlier, treat the first two (num = 0, num = 1) Fibonacci values as 0 and 1. Thus:
# rFib(2) = 1 (0+1)
# rFib(3) = 2 (1+1)
# rFib(4) = 3 (1+2)
# rFib(5) = 5 (2+3)
# rFib(3.65) = rFib(3) = 2
# rFib(-2) = rFib(0) = 0.

def rFib(num):
    if num <= 0: 
        return 0
    elif num == 1:
        return num
    return rFib(num-1) + rFib(num-2)

print(rFib(2))
print(rFib(3.65))
print(rFib(-2))