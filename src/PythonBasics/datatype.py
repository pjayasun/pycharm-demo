from itertools import zip_longest

print(type(5))

print(type(5.2))

print(type(5+6j))

a=5.6
b=int(a)
print(type(a), type(b))
print(a, b)

k=float(b)
print(type(k), k)

tf_value=True
print(type(tf_value))


a1=[1, 2]
a2=[3, 4]
c=zip(a1, a2)

for x, y in c:
    print(x, y)

str="Pranesh"
print(type(str))


keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict=dict(zip(keys, values))
print(my_dict)

pairs=[('a', 10), ('b', 20), ('c', 30)]
names, ages=zip(*pairs)

print(names, ages)



list1 = [1, 2]
list2 = [3, 4, 5]
for x, y in zip_longest(list1, list2, fillvalue=0):
    print(x, y)


names=["Pranesh", "Prathvika"]

for index, name in enumerate(names):
    print(f'index: {index}, name: {name}')

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

for x, y, z in zip(list1, list2, list3):
    print(x, y, z)  # Outputs: (1, 4, 7), (2, 5, 8), (3, 6, 9)

print(10<10 and 20==20)

x=True
print(x)

x=not x
print(x)
