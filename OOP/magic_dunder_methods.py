class Employee:
    # class variable
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, name, pay):
        self.first = first
        self.name = name
        self.pay = pay
        self.email = first + '.' + name + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.name, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


# __repr__ is meant to be an unambiguous representation of the object and should be used for debugging
# and logging and things like that
# __str__ is meant to be more of a readable representation
# of an object and is meant to be used as a display to the end user
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(len('test'))
print('test'.__len__())
print(len(emp_1))
print(emp_1 + emp_2)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

print(1 + 2)
print(int.__add__(1, 2))
print('a' + 'b')
print(str.__add__('a', 'b'))
