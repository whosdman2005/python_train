# Break
# Continue
# Else

# example for BREAK
for number in range(1, 11):
    if number == 5:
        break
    else:
        print(number)


# example for CONTINUE
for number in range(1, 11):
    if number == 5:
        continue
    else:
        print(number)


# example for ELSE
for number in range (1,11):
    if number == 15:
        break
    else:
        print(number)
else:
    print("All the numbers were printed without breaking the loop!")


# another example for ELSE
for number in range (1,11):
    if number == 5:
        break
    else:
        print(number)
else:
    print("All the numbers were printed without breaking the loop!!!")

