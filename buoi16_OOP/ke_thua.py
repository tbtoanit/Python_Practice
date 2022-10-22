class Person():
    name = ""
    age = 0
    address = ""
    def __init__(self):
        pass
    def insert(self):
        print("Insert New One")

class Human():
    pass

class Customer(Person):
    def check_points(self):
        print("Customer score calculation")

class Employee(Customer, Human):
    def calculation_salary(self):
        print("Employee Salary calculation function")

    #override/ghi đè
    def insert(self):
        print("Insert New One Employee")
