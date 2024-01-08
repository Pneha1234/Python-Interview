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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        # cls is the class

    @classmethod
    def from_string(cls, emp_str):
        first, name, pay = emp_str.split('-')
        return cls(first, name, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Stever-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)

#class methods can be used as alternative constructors

#static methods dont pass anything automatically
#static methods are just like normal functions but we include them in our classes because they have some logical
# connection with the class

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
