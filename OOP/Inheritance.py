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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, name, pay, prog_lang):
        super().__init__(first, name, pay)
        # Employee.__init__(self, first, name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, name, pay, employees=None):
        super().__init__(first, name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp  in self.employees:
            self.employees.append(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')
# print(help(Developer))
#
# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()