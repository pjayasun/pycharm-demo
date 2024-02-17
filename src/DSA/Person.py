import copy

class Person:
    def __init__(self, name):
        self.name = name


p = [Person("John"), Person("Tim"), Person("Pranesh")]

p1 = copy.deepcopy(p)

print(id(p[0]), id(p1[0]))
