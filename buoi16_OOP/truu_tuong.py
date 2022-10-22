from abc import ABC, abstractmethod  # abstract base class

class Person(ABC): #Lớp person là lớp trừu tượng
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass

class Customer(Person):
    name = ""
    age = 10
    address = ""
    def insert(self):
        print("Insert customer")
    def update(self):
        print("update customer")
    def delete(self):
        print("delete customer")

class Employee(Person):
    name = ""
    age = 20
    address = ""
    def insert(self):
        print("Insert employee")
    def update(self):
        print("update employee")
    def delete(self):
        print("delete employee")

e1 = Employee()

c1 = Customer()
