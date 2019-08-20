# https://www.youtube.com/watch?v=5qQQ3yzbKp8    <<<< reference

employees = ['Correy','Tom','John','Ben','Bob','Adam']

output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    print('Address of output is {}'.format(id(output)))

output += '</ul>'

print(output)

print('\n')

# OUTPUT
# Address of output is 29321408   <<<<<< everytime you add an entry from the list to build the HTML tags
# Address of output is 29352800   <<<<<< it creates a new string objects in memory
# Address of output is 29189328   <<<<<< Imagine if you have thousands in the list
# Address of output is 29164320   <<<<<< You'll have thousands of string objects that will affect performance
# Address of output is 28494720
# Address of output is 29284136
# <ul>
#	<li>Correy</li>
#	<li>Tom</li>
#	<li>John</li>
#	<li>Ben</li>
#	<li>Bob</li>
#	<li>Adam</li>
# </ul>
