
# Remove Blanks
#---------------------------------------------------------------------------------------------
# Create a function that, given a string, returns the string, without blanks. Given " play that
# Funky Music ", returns a string containing "playthatFunkyMusic".

string1 = " play that Funky Music "

def removeBlanks(string):
    newString =''
    for i in string:
        if ( i != ' '):
            newString += i
        else: 
            pass
    return newString

print(removeBlanks(string1))


# Get String Digits
#---------------------------------------------------------------------------------------------
# Create a python function that given a string, returns the integer made from the string’s
# digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1,357,924,680.

string2 = "0s1a3y5w7h9a2t4?6!8?0"

def getStringDigits(string):
    newString = ''
    for i in string:
        if (i.isdigit()):
            newString += i
        else: 
            pass
    return int(newString)

print(getStringDigits(string2))

# Acronyms
#---------------------------------------------------------------------------------------------
# Create a function that, given a string, returns the string’s acronym (first letters only,
# capitalized). Given "there's no free lunch - gotta pay yer way", return "TNFL-GPYW". Given
# "Live from New York, it's Saturday Night!", return "LFNYISN".

string3 = "there's no free lunch - gotta pay yer way"
string4 = "Live from New York, it's Saturday Night!"

def acronyms(string):
    words = string.split()
    newString = ''
    for i in words:
        newString += i[0]
    return newString.upper()

print(acronyms(string3))
print(acronyms(string4))

