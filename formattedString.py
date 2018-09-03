a = 1
b = 2
c = 3

sum = a + b + c
print ("{0} + {1} + {2} = {3}".format(a, b, c, sum))
# output 1 + 2 + 3 = 6

print (f"")  # this is called formatted strings new feature in python3

print (f"value of a is {a}") # make sure the f" are together otherwise it wont work
# output value of a is 1

print (f"value of b is {b}") # make sure the f" are together otherwise it wont work
# output value of b is 2

print (f"value of c is {c}") # make sure the f" are together otherwise it wont work
# output value of c is 3

print (f"sum of a and b is {a + b}")
# output sum of a and b is 3

print (f"{a} + {b} + {c} = {sum}")
# output 1 + 2 + 3 = 6
