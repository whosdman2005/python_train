def cubed(x):
    y = x**3

    return y

a=int(input("Enter a number to cube: "))

result = cubed(a)  # this will call the cubed function

print("The result of", str(a),"cubed is ", str(result))