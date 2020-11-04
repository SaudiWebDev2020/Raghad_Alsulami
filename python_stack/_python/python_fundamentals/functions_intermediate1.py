import random
def randInt(minimum=0, maximum=100):
    if (minimum < maximum and maximum > 0):
        num = random.random() * maximum + minimum
        return round(num)
        
print(randInt()) 		                    # should print a random integer between 0 to 100
print(randInt(minimum=0, maximum=50)) 	    # should print a random integer between 0 to 50
print(randInt(minimum=50, maximum=100 )) 	# should print a random integer between 50 to 100
print(randInt(minimum=50, maximum=500))    # should print a random integer between 50 and 500