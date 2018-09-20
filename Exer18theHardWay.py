# Names, Variables, Code, Functions

# this one is like your scripts with argv
def print_two(*args):                                                  # this will get any number of parameter inputs
    arg1, arg2 = args                                                  # It just happen we specify 2 variables that will be passed to the args
    print("arg1: %r, arg2: %r " % (arg1, arg2))                        # *args needs to be in parenthesis to WORK
                                                                       # this function DOES unpacking the (*args) then it will ask for arg1 & arg2

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):                                       # will use those 2 inputs; this function didnt need unpacking
    print("arg1: %r, arg2: %r " % (arg1, arg2))


# this just takes one argument
def print_one(arg1):                                                   # only 1 variable was needed
    print("arg1: %r" % (arg1))

# this one takes no argument
def print_none():                                                      # this will just use the function and shows the print out
    print("I've got nothin'.")


print_two("Led", "Zepplin")                                            # this is the input in the arg1 & arg2
print_two_again("Led", "Zeplin")                                       # this is the input in the arg1 & arg2 repeat
print_one("Una!")                                                      # this is the input for the single variable
print_none()                                                           # this will just call the function without any variables as input

# OUTPUT
# E:\GIT_DEV_python\venv\Scripts\python.exe E:/GIT_DEV_python/python_train/Exer18theHardWay.py
# arg1: 'Led', arg2: 'Zepplin'
# arg1: 'Led', arg2: 'Zeplin'
# arg1: 'Una!'
# I've got nothin'.


##############################################################################################
# the functions (or mini scripts) are mostly DEFINITIONS
# same as the "requirements.txt"
# variable declarations
# WHILE
# print_two("X","y") are the IMPLEMENTATIONS or rather USING the functions
