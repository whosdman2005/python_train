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
