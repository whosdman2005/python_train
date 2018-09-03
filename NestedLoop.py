# implementing matrix using Nested loops
# always use the latest python interpreter to make the "end with whitespaces" to work
# this is also tested in python 2.7 but complained about the END parameter


# 1 2 3
# 4 5 6
# 7 8 9

number = 1
for row in range(1, 4):
    for column in range(1, 4):
        print(number, end = ' ')
        number = number + 1
    print()
