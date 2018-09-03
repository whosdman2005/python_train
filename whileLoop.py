
# while loop, are used for repeating sections of code but unlike a for loop
# the while loop will not run "n" times but until a defined condition is no longer met.
# if the condition is initially false, the loop body will not be executed at all

temperature = 77
while temperature >= 68 and temperature <= 77:
    print("Room temperature is maintained at {} degree fahrenheit" .format(temperature))
    temperature = temperature -1


# while True:
#     print("This loop runs forever!!!")
#
# output
# This loop runs forever
# This loop runs forever
# This loop runs forever
# This loop runs forever
# This loop runs forever
# .....................

