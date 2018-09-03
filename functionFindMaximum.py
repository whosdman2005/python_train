# check which among the two numbers is maximum

def findMax(firstNum, secondNum):
    if firstNum > secondNum:
        print("First number is greater")
        return firstNum
    elif secondNum > firstNum:
        print("Second number is greater")
        return secondNum
    else:
        print("Both numbers are equal")
        return firstNum


print("Enter the first number: ")
firstNum = int(input())

print("Enter the second number: ")
secondNum = int(input())

findMax(firstNum, secondNum)
maximumNum = findMax(firstNum, secondNum)
print("Maximum number = {}".format(maximumNum))