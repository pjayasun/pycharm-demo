def greet(name):
    print(f"Hello, {name}")


name = input("Enter your name: ")
greet(name)


def greet(name="World"):
    print(f"Hello, {name}")


name = input("Enter your name: ")
greet()

def add(x, y):
    c = x + y
    return c

def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


d = add(198, 1)
print(d)

e, f = add_sub(198, 1)
print(e, f)

add = lambda x, y: x + y
print(add(5, 10))

