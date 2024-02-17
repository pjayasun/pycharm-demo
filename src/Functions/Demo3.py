def person(name, **kwargs):
    print(name)

    for key, value in kwargs.items():
        print(key+" "+str(value))


person("Pranesh", city="Boston", age=28)


"""
"""

a = 10
def something():
    a = 5
    x = globals()['a']
    globals()['a'] = 15
    print(id(x), id(a))

something()
print(a)