# Inheritance + subclass


class Employee:
    raise_amt = 1.04  # 4% raise

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}.format(self.first, self.last)'

    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    pass


dev1 = Developer('Tom', 'Lumba', 60000)
dev2 = Developer('Jerry', 'Binaba', 80000)

print (dev1.email)
print (dev2.email)

# print (help(Developer))  <<< to check the flow
# output
# Help on class Developer in module __main__:
# class Developer(Employee)
#  |  Methods inherited from Employee:
#  |
#  |  __init__(self, first, last, pay)
#  |
#  |  appy_raise(self)
#  |
# |  fullname(self)
# |
# |  ----------------------------------------------------------------------
# |  Data and other attributes inherited from Employee:
# |
# |  raise_amt = 1.04

# None
