# Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):          # the input variables will come from cheese_and_crackers 20  30
    print("You have %d cheeses!" % cheese_count)                   # 20 was the value that came from cheese_and_crackers variable
    print("You have %d boxes of crackers" % boxes_of_crackers)     # 30 was the value that came from cheese_and_crackers_variable
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)                                       # this will be the input for the function


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)         # 10, 50 will be the input from the variables above


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)                               # 30, 11 will be the input


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)    # 10 + 100, 50 + 1000 will be the input


# OUTPUT
# E:\GIT_DEV_python\venv\Scripts\python.exe E:/GIT_DEV_python/python_train/Exer19theHardWay.py
# We can just give the function numbers directly:
# You have 20 cheeses!
# You have 30 boxes of crackers
# Man that's enough for a party!
# Get a blanket.
#
# OR, we can use variables from our script:
# You have 10 cheeses!
# You have 50 boxes of crackers
# Man that's enough for a party!
# Get a blanket.
#
# We can even do math inside too:
# You have 30 cheeses!
# You have 11 boxes of crackers
# Man that's enough for a party!
# Get a blanket.
#
# And we can combine the two, variables and math:
# You have 110 cheeses!
# You have 1050 boxes of crackers
# Man that's enough for a party!
# Get a blanket.