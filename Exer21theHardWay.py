# Functions can return something

def add(a, b):                                                 # We are expecting 2 variables
    print("Adding %d + %d" % (a, b))                           # 30, 5
    return a + b                                               # whatever the 2 variables return the values to the add(35) function

def subtract(a, b):                                            # We are expecting 2 variables
    print("Subtracting %d - %d " % (a, b))                     # 78, 4
    return a - b                                               # 74

def multiply(a, b):                                            # We are expecting 2 variables
    print("Multiplying %d * %d" % (a, b))                      # 90, 2
    return a * b                                               # 180

def divide(a, b):                                              # We are expecting 2 variables
    print("Divide %d / %d" % (a, b))                           # 100, 2
    return a / b                                               # 50.0

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# Output
# E:\GIT_DEV_python\venv\Scripts\python.exe E:/GIT_DEV_python/python_train/Exer21theHardWay.py
# Let's do some math with just functions!
# Adding 30 + 5
# Subtracting 78 - 4
# Multiplying 90 * 2
# Divide 100 / 2
# Age: 35, Height: 74, Weight: 180, IQ: 50
# Here is a puzzle.
# Divide 50 / 2
# Multiplying 180 * 25
# Subtracting 74 - 4500
# Adding 35 + -4426
# That becomes:  -4391.0 Can you do it by hand?
