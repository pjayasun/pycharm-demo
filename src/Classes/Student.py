class Student:
    count = 0

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.count = Student.attendance()

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def attendance(cls):
        cls.count += 1
        return cls.count

    @classmethod
    def get_total(cls):
        return cls.count

    @staticmethod
    def info():
        print("This is a student class")


student1 = Student(100, 90, 80)
student2 = Student(69, 100, 78)


print(student1.average())
print(student2.average())

print(Student.get_total())
Student.info()