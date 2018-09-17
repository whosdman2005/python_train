# Reading files

from sys import argv                              # sys is a PACKAGE and the argv is a FEATURE in that package

script, filename = argv                           # the script itself and whatever filename the user type will be passed to argv variable

txt = open(filename)                              # the open action will OPEN the filename from the argv

print("Here's your file %r:" % filename)
print(txt.read())                                # This will read the variable txt
txt.close()


print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()

# Output
# (venv) E:\GIT_DEV_python\python_train>python Exer15theHardWay.py ex15_sample.txt
# Here's your file 'ex15_sample.txt':
# This stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.
# Type the filename again:
# > ex15_sample.txt
# This stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.


# Note:
# ALWAYS close your stream especially when you READ/WRITE a file
