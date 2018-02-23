student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Biology']}
student['phone'] = '555-5555'  # adding or updating to the list
student['name'] = 'Jane'    # adding or updating to the list

student.update({'name': 'Panda'})

print (student)
# output  {'courses': ['Math', 'Biology'], 'age': 25, 'name': 'John'}

print (student['age'])
# output  25

print (student['courses'])
# output  ['Math', 'Biology']

print (student.get('name'))
# using GET method
# output John

print (student.get('phone'))
# using GET method if it doesnt exist
# output None

print (student.get('phone', 'nOt fOunD'))
# using GET method if it doesnt exist
# output nOt fOunD
