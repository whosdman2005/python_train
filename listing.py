# tuples, lists and sets

courses = ['History', ' Physics', 'Science', 'PE', 'Recess']
courses_2 = ['Chemistry', 'English']
numb = [6, 3, 2, 5, 7, 1, 4]

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

courses.pop()
print(courses)
# output ['Art', 'History', ' Physics', 'Science', 'PE', 'Recess', 'Art', 'Chemistry']

popped = courses.pop()
print(popped)
print(courses)
# output Chemistry   <<< had been popped out from the list
# ['Art', 'History', ' Physics', 'Science', 'PE', 'Recess', 'Art']

courses.reverse()
print(courses)
# output ['Art', 'Recess', 'PE', 'Science', ' Physics', 'History', 'Art']

courses.sort()
print(courses)
# output ['Physics', 'Art', 'Art', 'History', ' PE', 'Recess', 'Science']

numb.sort()
print (numb)
# output [1, 2, 3, 4, 5, 6, 7]
