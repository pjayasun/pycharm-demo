class Student:
    def __init__(self, name, rollno, age, model, price):
        self.name = name;
        self.rollno = rollno
        self.age = age
        self.lap = self.Laptop(model, price)

    def show(self):
        print(f'Name: {self.name}, Rollno: {self.rollno}, Age: {self.age}')
        self.lap.show()

    class Laptop:
        def __init__(self, model, price):
            self.model = model
            self.price = price

        def show(self):
            print(f'Model: {self.model}, Price: {self.price}')


student1 = Student("Pranesh", 1011, 28, "Macbook Pro", 1000)
student1.show()
