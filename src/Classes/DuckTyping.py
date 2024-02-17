class Duck:
    def quack(self):
        print("Quack, quack")


class Person:
    def quack(self):
        print("I am quacking like a duck")


def display(something):
    something.quack()


d = Duck()
p = Person()

display(d)
display(p)
