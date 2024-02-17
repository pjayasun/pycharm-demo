class Greet:

    """
    We can consider __init__ as constructors in java
    """
    def __init__(self, name):
        print("Inside init")
        self.name = name

    def welcome(self):
        print("Welcome,",self.name)





# Instance creation
person_1 = Greet("Fabian")
person_1.welcome()

print()

person_2 = Greet("Christopher")
Greet.welcome(person_2)
