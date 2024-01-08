from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


comp = Computer()
comp.process()

#
# class Laptop(Computer):
#     def process(self):
#         print("Its running")
#
# lap = Laptop()
# lap.process()

