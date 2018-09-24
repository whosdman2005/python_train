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



