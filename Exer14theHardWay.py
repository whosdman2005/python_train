# Prompting and Passing

from sys import argv

script, user_name = argv
prompt = '$>'

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print ("""
Alright, so you said %r about liking me.
You live in %r. Not sure  where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))

# Output
# E:\GIT_DEV_python\python_train>python Exer14theHardWay.py Tom
# Hi Tom, I'm the Exer14theHardWay.py script.
# I'd like to ask you a few questions.
# Do you like me Tom?
# >Yes
# Where do you live Tom?
# >In the house
# What kind of computer do you have?
# >ASUS
#
# Alright, so you said 'Yes' about liking me.
# You live in 'In the house'. Not sure  where that is.
# And you have a 'ASUS' computer. Nice.
#


