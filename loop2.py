courses = ['History', 'Science', 'Math', 'Biology']

for index, course in enumerate(courses):
    print (index, course)
# output
# (0, 'History')
# (1, 'Science')
# (2, 'Math')
# (3, 'Biology')

# if you dont want to start the index at ZERO
for index, course in enumerate(courses, start=1):
    print (index, course)
# output
# (1, 'History')
# (2, 'Science')
# (3, 'Math')
# (4, 'Biology')
