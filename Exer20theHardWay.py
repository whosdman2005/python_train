# Functions and Files

from sys import argv

script, input_file = argv

def print_all(f):                                    # this function will display the desired file that will be passed to variable f
    print(f.read())

def rewind(f):                                       # This function will go to current position in the file to start that will be passed to variable f
    f.seek(0)

def print_a_line(line_count, f):                     # this function will display the line count first then the whole line from the variable f
    print(line_count, f.readline())

current_file = open(input_file)                      # this will display it

print("First let's print the whole file:\n")

print_all(current_file)                               # This step will display or OPEN the desired file

print("Now let's rewind, kind of like a tape.")

rewind(current_file)                                  # this step will just go to the start of the desired file

print("Let's print three lines:")

current_line = 1                                      # we initialize the "start" of the file
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)


# Output
# E:\GIT_DEV_python\python_train>python Exer20theHardWay.py test.txt
# First let's print the whole file:
#
# the quick brown fox
# jumps over the lazy
# dog that will hunt your ass off
#
# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 the quick brown fox
#
# 2 jumps over the lazy
#
# 3 dog that will hunt your ass off


# notes:
# What is f in the print_all and other functions?
# The f is a variable just like you had in other functions in Exer18theHardWay.py except this time it's a file.
# A file in python is kind of like an old tape drive on a mainframe, or maybe a DVD player. It has a "read head" and you
# can "seek" this read head around the file to positions, then work with it there. Each time you do f.seek(0), you're
# moving to the start of the file. Each time you do f.readline(), you're reading a line from the file and moving the read head
# to the right after the \n (new line) that ends that file.

# Why does seek(0) not set the current_line to 0?
# First, the seek() function is dealing in bytes, not lines. So thats going to the 0 byte (first byte) in the file.
# Second current_line is just a variable and has no real connection to the file at all. We are manually incrementing it.