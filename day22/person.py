class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name is {self.name}. Age is {self.age}"


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        self.salary = salary
        self.designation = designation
        super().__init__(name, age)

    def get_details(self):
        print(super().get_details())
        return f"Salary is {self.salary}. Designation is {self.designation}"


e1 = Employee("Jon", 45, 30000, "teacher")
print(e1.get_details())

