employees = ['Correy','Tom','John','Ben','Bob','Adam']

output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    # print 'Address of output is {}'.format(id(output))

output += '</ul>'

print(output)

print('\n')