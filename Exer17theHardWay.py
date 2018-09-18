# More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv                               # here are the input variables to be passed to argv

print("Copying from %s to %s" % (from_file, to_file))           # this will display the FROM and TO file

# we could do these two on one line too, how?

in_file = open(from_file)                                       # This will open the FROM file
indata = in_file.read()                                         # This step will read the file

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()                                                         # Is a prompt that waits for user input

out_file = open(to_file, 'w')                                   # This will open the NEW file with WRITE permission
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


# Output
# (venv) E:\GIT_DEV_python\python_train>python Exer17theHardWay.py test.txt new_file.txt
# Copying from test.txt to new_file.txt
# The input file is 72 bytes long
# Does the output file exist? False
# Ready, hit RETURN to continue, CTRL-C to abort.
#
# Alright, all done.
