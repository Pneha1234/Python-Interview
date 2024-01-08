class Employee:
    def __init__(self, first, name):
        self.first = first
        self.name = name

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.name)

    @property
    def email(self):
        return '{} .{}@emil.com'.format(self.first, self.name)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.name = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.name = None


emp_1 = Employee('Corey', 'Schafer')
emp_1.first = 'Jim'
emp_1.fullname = 'Corey1 Schafer1'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname