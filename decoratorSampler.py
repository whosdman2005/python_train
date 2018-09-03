# this is an example on how to use decorators
# decorators can solve the speed/performance of each functions


# this is an example of functions
import time #this will add a timer in order to check the time from-to of execution inside the function


# def calc_square(numbers):
#     start = time.time() # start of the timer                                                                       CODE DUPLICATION
#     result = []
#     for number in numbers:
#         result.append(number*number)
#     end = time.time()  #end of the timer                                                                           CODE DUPLICATION
#     print(("calc_square took " + str((end-start) * 1000)) + " milli sec") #just a printout                         CODE DUPLICATION
#     return result
#
#
# def calc_cube(numbers):
#     start = time.time()  # start of the timer                                                                      CODE DUPLICATION
#     result = []
#     for number in numbers:
#         result.append(number*number*number)
#     end = time.time()  # end of the timer                                                                          CODE DUPLICATION
#     print(("calc_square took " + str((end - start) * 1000)) + " milli sec")  # just a printout                     CODE DUPLICATION
#     return result
#
#
# array = range(1,100000)
# out_square = calc_cube((array))
# out_cube = calc_cube(array)


# Decorators solve both of these issues:
#     Code duplication
#     cluttering main logic of function with additional functionality (i.e timing in our example)

def time_it(func):                                                                 # Structure for decorators
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func (*args, ** kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start) * 1000) + " milli sec")
        return result
    return wrapper

@time_it                                                                           # Implementing decorators
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


@time_it                                                                           # Implementing decorators
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


array = range(1,100000)
out_square = calc_cube((array))
out_cube = calc_cube(array)


# note:
# Function are first class objects in python. What it means is that they can be treated just like any other
# variable and you can pass them as an argument to another function or even return them as a return value


# Another note:
# Decorators act as a wrapper for your original function
# Common use cases of decorators are Logging & Timing