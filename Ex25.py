def MyMax(firstnumber, secondnumber):
    if firstnumber > secondnumber:
        return firstnumber
    else:
        return secondnumber

numbers=input("Enter two numbers separated by a comma: ")
list = numbers.split(",")

firstnumber = list[0]
secondnumber = list[1]

result = MyMax(firstnumber, secondnumber)

print(result, "is the greater of the two numbers.")

