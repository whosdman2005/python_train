def add(arg1=10, arg2=40, arg3=50):
    return arg1 + arg2 + arg3

add()

# Output 100

g = lambda x = 10, y = 40, z = 50: x + y + z
g(200, 400, 12)
# Output 612


def check(num):
    return num % 2 == 0 or num > 8

check(8)

# Output True

g2 = lambda num: num % 2 == 0 or num > 8
g2(4)
# Output True
g2(5)
# Output False