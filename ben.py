# this is the library to be used by functionsCBT.py


def helloWorld():
    print("Hello World!!!")


def exp(x,y):
    z = x ** y
    print(z)


def prinFib(n):
    a, b = 0,1
    while b < n:
        print(b)
        a,b = b, a+b

def calcFib(n):
    result = []
    a, b = 0,1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result



