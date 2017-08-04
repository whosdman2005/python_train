# tuples, lists and sets
# list = mmutable (can be modified)
# tuples = immutable (cannot be modified)


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
# sorting via method
# output Chemistry   <<< had been popped out from the list
# ['Art', 'History', ' Physics', 'Science', 'PE', 'Recess', 'Art']

courses.reverse()
print(courses)
# sorting via method
# output ['Art', 'Recess', 'PE', 'Science', ' Physics', 'History', 'Art']

courses.sort()
print(courses)
# sorting via method
# output ['Physics', 'Art', 'Art', 'History', ' PE', 'Recess', 'Science']

numb.sort()
print (numb)
# sorting via method
# output [1, 2, 3, 4, 5, 6, 7]

courses.sort(reverse=True)
print(courses)
# sorting via method
# output ['Science', 'Recess', 'PE', 'History', 'Art', 'Art', ' Physics']

numb.sort(reverse=True)
print (numb)
# sorting via method
# output [7, 6, 5, 4, 3, 2, 1]

sorted_courses = sorted(courses)
print(sorted_courses)
# sorting via function "sorted"
# output [' Physics', 'Art', 'Art', 'History', 'PE', 'Recess', 'Science']

print(min(numb))
# output 1

print(max(numb))
# output 7

print(sum(numb))
# output 28

print ('Biology' in courses)
# output False   because Biology doesnt exist in the courses list  "in" is a method

for sample in courses:
    print sample
# output
# Science
# Recess
# PE
# History
# Art
 # Art
 # Physics

# for index, courses in enumerate(courses):
#    print(index, courses)
# output it shows the courses with its index value
# (0, 'Science')
# (1, 'Recess')
# (2, 'PE')
# (3, 'History')
# (4, 'Art')
# (5, 'Art')
# (6, ' Physics')

# for index, courses in enumerate(courses, start=1):
#    print(index, courses)
# output it shows the courses with its index value but we want to start at number 1 instead of ZERO
# (1, 'Science')
# (2, 'Recess')
# (3, 'PE')
# (4, 'History')
# (5, 'Art')
# (6, 'Art')
# (7, ' Physics')

course_str = ' , '.join(courses)
print (course_str)
# output Science , Recess , PE , History , Art , Art ,  Physics

course_str = ' - '.join(courses)
print (course_str)
# output Science - Recess - PE - History - Art - Art -  Physics
