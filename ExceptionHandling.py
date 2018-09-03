# try:
#     length = 10
#     # width = 0
#     length / width
#
# except Exception:
#     print("Division by zero is invalid! Kindly change your input!!!")

# the above instructions is fine EXCEPT if the parameter width had been deleted
# when it run it will automatically go to the "except" since the EXCEPTION is a generic capture
# the best practice is get the results and get the error name and pass it to the except

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'width' is not defined

# another example
# try:
#     length / width # here width variable was deleted therefore length / 0 will raise the EXCEPT block
#
# except NameError:
#     print("Variable has been used before defining it")

# Output
#    Variable has been used before defining it

# another example
try:
    width = 0
    length = 10

    length / width

except NameError:
    print("Variable has been used before defining it")
except ZeroDivisionError:
    print("Division by zero is invalid! Kindly change your input")