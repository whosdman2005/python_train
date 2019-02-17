# Lambda

# add x and y
def add (x, y):
    return x + y

# in lambda form it will be
lambda x, y: x + y

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# max of x, y
def mx (x, y):
    if x > y:
        return x
    else:
        return y

print(mx(8,5))

# in lambda form
mx = lambda x, y: x if x > y else y
print (mx(8,5))


