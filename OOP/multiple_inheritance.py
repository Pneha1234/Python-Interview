class Calculations:
    def sum(self, a, b):
        return a + b

class MoreCalculations:
    def multiply(self, a, b):
        return a * b

class DerivedCalculations(Calculations, MoreCalculations):
    def divide(self, a, b):
        return a / b

d = DerivedCalculations()
print(d.sum(10, 20))
print(d.multiply(10, 20))
print(d.divide(10, 20))
print(DerivedCalculations.mro())