# from cyberuniversity
# Program to determine whether a shape is a rectangle or a square and calculate its area and perimeter

height = float(input("Enter the height of the shape: "))

length = float(input("Enter the width of the shape: "))

if (height == length):
    shape = "square"

else:
    shape = "rectangle"


area = (height * length)
perimeter = ((length + height) * 2)

print ("The shape is a", shape, "with an area of", area, "and perimeter of", perimeter)
