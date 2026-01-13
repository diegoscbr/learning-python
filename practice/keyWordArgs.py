'''
Docstring for keyWordArgs
* Keyword argument = an argument proceeeded by an identifier
* helps with readability
* order of arguments does not matter
1. positional 2. default 3. KEYWORD 4. arbitrary
'''
#notice how the end and sep keyword args superceed the default \n arg
for x in range(1, 11):
    print(x, end = "--> ")
print(" ")
print("1", "2", "3", "4", sep="()")

def getPhone(country, area, firstThree, lastFour):
    return f"+{country}-{area}-{firstThree}-{lastFour}"

print(getPhone(firstThree=606, area=619, country=1, lastFour=6774))
