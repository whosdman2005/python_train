# Strings and Text

x = ("There are %d types of people." %10)  # the %10 will be placed to the %d since its a decimal value
binary = ("binary")
do_not = ("don't")
y = ("Those who %s and those who %s." %(binary, do_not)) # the %s is where the binary & do_not value

print(x)  # This will print the whole string of x variable
print(y)  # This will print the whole string of y variable

print ("I said: %r." %x)  # %r was from repr() and its used for debugging it will display the RAW data
print ("I also said: '%s'." %y)

hilarious = False
joke_evaluation = ("Isn't that joke so funny?! %r")

print (joke_evaluation %hilarious)

w = ("This is the left side of ...")
e = ("a string with a right side.")

print(w+e)  # This one is string concatination

