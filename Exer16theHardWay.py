# Reading and Writing Files

# close - Closes the file. like File > Save... in your Editor
# read - Read the contents of the file. You can assign the result to a variable
# readline - Reads just ONE line of a text file
# truncate - Empties the file. Watch out if you care about the file
# write(stuff) - Write stuff to the file

from sys import argv                                         # sys package will use argv feature to this script

script, filename = argv                                      # variable script and filename will be the input parameter

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")                                                   # this is just a prompt sign

print("Opening the file......")
target = open(filename, 'w')                                 # this will open the filename with WRITE permissions

print("Truncating the file. Goodbye!")
target.truncate()                                            # this will truncate the contents of the filename/file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")                                    # this lines will be your INPUT stream
line2 = input("line 2. ")                                    # you can type how many sentences you want
line3 = input("line 3. ")                                    # and it will WRITE to the filename/file

print("I'm going to write these to the file.")

target.write(line1)                                          # this is the actual WRITE of the process in line1
target.write("\n")                                           # new line will just be implemented
target.write(line2)                                          # this is the actual WRITE of the process in line2
target.write("\n")                                           # new line will just be implemented
target.write(line3)                                          # this is the actual WRITE of the process in line3
target.write("\n")                                           # new line will just be implemented

print("And finally, we close it.")
target.close()                                               # closing the stream
