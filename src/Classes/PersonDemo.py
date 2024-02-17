class Person:
    id = 0

    def __init__(self, name, age):
        self.id = Person.generate_id()
        self.name = name
        self.age = age

    def update(self):
        self.name = "Hello, " + self.name
        self.age = self.age + 5

    def compare(self, p):
        if self.age == p.age:
            return True
        else:
            return False

    def toString(self):
        return f'ID: {self.id}, Name: {self.name}, Age: {self.age}'

    @classmethod
    def generate_id(cls):
        cls.id += 1
        return cls.id


p1 = Person("Pranesh", 20)
p2 = Person("Prathvika", 20)
p3 = Person("Mango", 15)

p1.update()

print(p1.toString())
print(p2.toString())
print(p3.toString())

if p1.compare(p2):
    print("Same")
else:
    print("Different")
