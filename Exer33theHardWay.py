# While Loops

# to avoid problems for while loops
# 1. Make sure that you use while loops sparingly. Usually a for-loop is better.
# 2. Review your while statements and make sure that the thing you are testing will become FALSE at some point
# 3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what its doing.

i = 0
numbers = []

while i < 6:
    print("At the top i is %d" %i)
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" %i)

print("The numbers: ")

for num in numbers:
    print(num)

# OUTPUT
# E:\GIT_DEV_python\venv\Scripts\python.exe E:/GIT_DEV_python/python_train/Exer33theHardWay.py
# At the top i is 0
# Numbers now:  [0]
# At the bottom i is 1
# At the top i is 1
# Numbers now:  [0, 1]
# At the bottom i is 2
# At the top i is 2
# Numbers now:  [0, 1, 2]
# At the bottom i is 3
# At the top i is 3
# Numbers now:  [0, 1, 2, 3]
# At the bottom i is 4
# At the top i is 4
# Numbers now:  [0, 1, 2, 3, 4]
# At the bottom i is 5
# At the top i is 5
# Numbers now:  [0, 1, 2, 3, 4, 5]
# At the bottom i is 6
# The numbers:
# 0
# 1
# 2
# 3
# 4
# 5


# What's the difference between a FOR-Loop and a WHILE-Loop?
# A FOR-Loop can only iterate (loop) "over" collections of things. A WHILE-Loop can do any kind of iteration (looping) you want.
# However, WHILE-Loops are harder to get right and you normally can get many things done with FOR-Loops

