# set uses curly braces
# sets throw away duplicate in the list
# every execution the list changes because SETs doesnt care about order

cs_courses1 = {'History', 'Biology', 'Math', 'Physics', 'CompSci', 'Math'}
cs_courses2 = {'History', 'Biology', 'Math', 'Physics', 'CompSci'}
art_courses = {'Art', 'History', 'CompSci', 'Design'}

print (cs_courses1)
# output set(['Biology', 'CompSci', 'Physics', 'Math', 'History'])

print ('Biology' in cs_courses1)
# output True
# set is optimized in checking values in the list compared to lists/tuples

print (cs_courses2.intersection(art_courses))
# These are the subjects in common with cs_courses2 & art_courses
# output  set(['Biology', 'CompSci', 'Physics', 'Math', 'History'])

print (cs_courses2.difference(art_courses))
# output
