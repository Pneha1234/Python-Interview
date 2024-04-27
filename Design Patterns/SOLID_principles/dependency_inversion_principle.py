# the dependency inversion principle(DIP): Abstractions should not depend upon details. Details should depend upon
# abstractions.

# example:-
# app_dip.py

class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"

# In this example, the FrontEnd class depends on the BackEnd class and its concrete implementation. You can say that
# both classes are tightly coupled. This coupling can lead to scalability issues. For example, say that your app is
# growing fast, and you want the app to be able to read data from a REST API. How would you do that?

# You may think of adding a new method to BackEnd to retrieve the data from the REST API. However, that will also
#  require you to modify FrontEnd, which should be closed to modification, according to the open-closed principle.

# To fix the issue, you can apply the dependency inversion principle and make your classes depend on abstractions rather
# than on concrete implementations like BackEnd. In this specific example, you can introduce a DataSource class that
# provides the interface to use in your concrete classes:

# app_dip.py

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"