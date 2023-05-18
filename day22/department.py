class Department:
    def __init__(self, name, no_of_students):
        self.name = name
        self.no_of_students = no_of_students

    def get_total(self, *args):
        return self.no_of_students + sum([i.no_of_students for i in args])


d1 = Department("CS", 50)
d2 = Department("Elex", 40)
d3 = Department("Computer", 10)

print(d1.get_total(d2, d3))
