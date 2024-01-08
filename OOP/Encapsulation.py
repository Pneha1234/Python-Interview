class Payment:
    def __init__(self, amount):
        self.__amount = amount + amount * 0.05

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount, discount):
        self.__amount = self.__amount - self.__calculate_discount(amount, discount)


    def __calculate_discount(self, amount, discount):
        return amount *(discount/100)

book = Payment(100)
print(dir(book))
book._Payment__calculate_discount(100, 10)
book.set_amount(100, 10)
print(book.get_amount())

# private variables are not accessible outside the class
# protected variables are accessible outside the class but only in the child class