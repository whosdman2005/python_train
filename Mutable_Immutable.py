# Strings are immutable

a = 'corey'
print(a)
print('Address of a is: {}'.format(id(a)))

a = 'jon'
print(a)
print('Address of a is: {}'.format(id(a)))


# OUTPUT
# corey
# Address of a is: 18210240  <<<<<<< Memory object are NOT the same
# jon
# Address of a is: 18210336  <<<<<<< Memory object are NOT the same

# a[0] = 'C'
# print(a)

# corey
# Address of a is: 58908096
# Traceback (most recent call last):
# jon
# Address of a is: 58908192
#   File "E:/GIT_DEV_python/python_train/Mutable_Immutable.py", line 18, in <module>
#     a[0] = 'C'
# TypeError: 'str' object does not support item assignment
# Since string is IMMUTABLE you cant overwrite a particular field in the LIST


# LIST data structure are MUTABLE
b = [1,2,3,4,5,6,7]
print(b)
print('Address of a is: {}'.format(id(b)))

b[0] = '9'
print(b)
print('Address of a is: {}'.format(id(b)))

# OUTPUT
# [1, 2, 3, 4, 5, 6, 7]
# Address of a is: 2897320  <<<<<<< Memory object are the same

# ['9', 2, 3, 4, 5, 6, 7]   <<<<<<< yet it changed the LIST
# Address of a is: 2897320  <<<<<<< Memory object are the same
