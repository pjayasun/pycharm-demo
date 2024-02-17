import array as arr

vals = arr.array('i', [1, 2, 3, 4])
vals.reverse()
print(vals[0])

t = (1, 2, 3)
u = tuple(reversed(t))
print(t, u)

v = u[::-1]
print(t, u, v)

for i in range(len(vals)):
    print(vals[i])

vals_array = arr.array(vals.typecode, [100, 200, 300])

for i in range(len(vals_array)):
    print(vals_array[i])

vals_array = arr.array(vals.typecode, (a for a in vals))

for i in range(len(vals_array)):
    print(vals_array[i])

print()
print()
print()

add = lambda x, y: x + y
print(add(2, 4))

a = [90, 45, 13, 1]
b = (4, 3, 1, 5, 6)

a.sort()
c = sorted(b)
d = tuple(c)
print(a, d)

list_of_tuples = [(1, 'd'), (2, 'b'), (3, 'c'), (4, 'a')]
list_of_tuples.sort(key=lambda x: x[0])
print(list_of_tuples)

squared = map(lambda x: x ** 2, b)
print(a, list(squared))

temp = arr.array('i', [])
length = int(input("Enter the length: "))

for i in range(length):
    temp.append(int(input("Enter the element: ")))

print(temp)

search_value = int(input("Enter the element to search for: "))

for index, i in enumerate(temp):
    if search_value == i:
        print(index)
        break
else:
    print("Not found")

print(temp.index(search_value))
