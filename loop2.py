courses = ['History', 'Science', 'Math', 'Biology']

course_str = ', '.join(courses)  # converting the list into Strings

course_str = ' - '.join(courses)

new_list = course_str.split(' - ')  # converting the String into new list

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

print (course_str)
# if course_str = ', '.join(courses)
# output History, Science, Math, Biology

print (course_str)
# if course_str = ' - '.join(courses)
# output History - Science - Math - Biology

print (course_str)
print (new_list)
# output
# back into list ['History', 'Science', 'Math', 'Biology']
