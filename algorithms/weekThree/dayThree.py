# Parens Valid
# ----------------------------------------------------------------------------------------
# Create a function that, given an input string, returns a boolean whether parentheses in that string are valid. 
# Given input "y(3(p)p(3)r)s", return true. Given "n(0(p)3", return false. Given "n)0(t(0)k", return false.

string = "y(3(p)p(3)r)s"
string2 = "n(0(p)3"
string3 = "n)0(t(0)k"

def parensValid(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            if (count == 0):
                return False
            count -= 1
    return False if count != 0 else True 

print(parensValid(string))
print(parensValid(string2))
print(parensValid(string3))



# Braces Valid
# ----------------------------------------------------------------------------------------
# Given a string, returns whether the sequence of various parentheses, braces and brackets within it are valid. 
# For example, given the input string "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!", return true. Given "d(i{a}l[t]o)n{e", 
# return false. Given "a(1)s[O(n]0{t)0}k", return false.

string4 = "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!"
string5 = "d(i{a}l[t]o)n{e"
string6 = "a(1)s[O(n]0{t)0}k"

def bracesValid(string):
    count = 0
    for i in string:
        if i == '(' or i == '[' or i == '{':
            count += 1
        if i == ')' or i == ']' or i == '}':
            if (count == 0):
                return False
            count -= 1
    return False if count != 0 else True 

print(bracesValid(string4))
print(bracesValid(string5))
print(bracesValid(string6))