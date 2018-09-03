# this is an exercise in functions from udemy
# Programming with Python: Hands-On Introduction for Beginners
# compute the area of rectangle

# A RETURN statement returns the value which will be stored in a variable
#
# A PRINT statement just prints it onto your screen

lengthOne = 8
widthOne = 3
lengthTwo = 10
widthTwo = 4

# this is the solution but NOT in a function
areaOne = lengthOne * widthOne
areaTwo = lengthTwo * widthTwo

# print(areaOne)
# print(areaTwo)

# This is the solution using a FUNCTION

def computeArea(length, width):
    area = length * width
    print(area)

def computeArea(length, width):
    area = length * width
    return area


def findMaximum(numberOne, numberTwo):
    if numberOne > numberTwo:
        return numberOne
    else:
        return numberTwo




# computeArea(4, 6)
computeArea(lengthOne, widthOne)
computeArea(lengthTwo, widthTwo)
areaOne = computeArea(lengthOne, widthOne)
areaTwo = computeArea(lengthTwo, widthTwo)


numberOne = 10
numberTwo = 20
greaterNumber = findMaximum(numberOne, numberTwo)



