class Employee:
    #class variable
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, name, pay):
        self.first = first
        self.name = name
        self.pay = pay
        self.email = first + '.' + name + '@company.com'

        Employee.num_of_emps+= 1

    def fullname(self):
        return '{} {}'.format(self.first, self.name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)




#instance variables contain data that is unique to each instance
#Class variables are variables that are shared among all instances of a class
#Self is the instance of the class
print(Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.__dict__)
print(Employee.__dict__)

emp_1.raise_amount =1.05
print(emp_1.__dict__)


print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)