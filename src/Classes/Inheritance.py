class A:

    def __init__(self):
        print("A init")

    def feature1(self):
        print("Feature 1 A")

    def feature2(self):
        print("Feature 2")


class B:
    def __init__(self):
        super().__init__()
        print("B init")


    def feature1(self):
        print("Feature 1 B")

    def feature4(self):
        print("Feature 4")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")

    def feature5(self):
        print("Feature 5")

    def feature6(self):
        print("Feature 6")


c = C()
c.feature1()
print(C.__mro__)

