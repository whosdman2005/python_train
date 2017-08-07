# if you need to do looping and access to the list use TUPLES
# if you need something to modify use LIST


# Mutable
list_1 = ['History', 'Science', 'Religion', 'Math', 'Physics', 'Chemistry', 'Drafting']
list_2 = list_1

print (list_1)
print (list_2)
# output
# ['History', 'Science', 'Religion', 'Math', 'Physics', 'Chemistry', 'Drafting']
# ['History', 'Science', 'Religion', 'Math', 'Physics', 'Chemistry', 'Drafting']

list_1[0] = '_Art_'
print (list_1)
print (list_2)
# output
# ['_Art_', 'Science', 'Religion', 'Math', 'Physics', 'Chemistry', 'Drafting']
# ['_Art_', 'Science', 'Religion', 'Math', 'Physics', 'Chemistry', 'Drafting']

# Immutable
tuple_1 = ('History', 'Science', 'Religion', 'Math', 'Physics', 'Chemistry', 'Drafting')
tuple_2 = tuple_1

print (tuple_1)
print (tuple_2)
# output
# ('History', 'Science', 'Religion', 'Math', 'Physics', 'Chemistry', 'Drafting')
# ('History', 'Science', 'Religion', 'Math', 'Physics', 'Chemistry', 'Drafting')

tuple_1[0] = 'Art'

print (tuple_1)
print (tuple_2)
# output since its Immutable we cannot modify/delete to the list
#     tuple_1[0] = 'Art'
# TypeError: 'tuple' object does not support item assignment

# you can do everything just like in the list
# EXCEPT changing/deleting  the list since its IMMUTABLE
