# tuples, lists and sets

courses = ['History', ' Physics', 'Science', 'PE', 'Recess']
courses_2 = ['Chemistry', 'English']


print (courses[2:])  # slicing technique
# output ['Art', 'History', ' Physics', 'Science', 'PE', 'Recess', 'Art']

courses.append('Art')  # this will append Art to the lists
print(courses)
#output ['History', ' Physics', 'Science', 'PE', 'Recess', 'Art']

courses.insert(0, 'Art')  # this will insert Art to the lists
print(courses)
# output ['Art', 'History', ' Physics', 'Science', 'PE', 'Recess', 'Art']

# this method will extend whatever in courses + coursers2 to the final list
courses.extend(courses_2)
print(courses)
# output ['Art', 'History', ' Physics', 'Science', 'PE', 'Recess', 'Art', 'Chemistry', 'English']
