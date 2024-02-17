def update(x):
    print(id(x))
    x = 8;
    print(id(x))
    print(x)
    return x


a = 10
print(id(a))
update(a)
print(id(a))
print(a)


def modify_elements(seq):
    seq.append(10)
    seq = [1, 2, 3, 4, 5]
    print(seq)


list_1 = [1, 2, 3]
modify_elements(list_1)
print(list_1)


def person(age, name="Default"):
    print(name)
    print(age - 2)


person(28, "Pranesh")
person(age=28, name="Pranesh")
person(age=28)


# Variable length arguments

def add(*args):
    print(sum(args))


add(4, 5, 6, 7)