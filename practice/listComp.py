'''
Docstring for listComp

List Comprehension = a consice way to create lists in Python
Compact and easier to read than traditional loops
FORMULA: [expression for value in iterabl if condition]

'''

#traditional list instance
doubles = []
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)
#list comp
#doublesToo = [expression for value in iterabl if condition]

doublesToo = [x * 2 for x in range(1,11)]
print(doublesToo)

triples = [y * 3 for y in range(1,11)]
print(triples)


# using conditional statements in list comprehension
negandPos = range(-10,11)
strictlyPos = [x for x in negandPos if x >=0]
strictlyNeg = [x for x in negandPos if x <=0]
print(strictlyPos)
print(strictlyNeg)

grades = [85, 65, 32, 61, 30, 45]
passingGrades = [grade for grade in grades if grade >= 65]
print(passingGrades)