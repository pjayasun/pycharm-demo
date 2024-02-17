candies = int(input("How many candies do you want?"))
available_candies = 5

i = 1
while(i <= candies):
    if i > available_candies:
        print("Sorry, out of stock")
        break
    print("Candy")
    i += 1
print("Byeeee")


for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

x = [1, 2, 3, 4, 5]
y = [i for i in x if i>3]

print(x, y)

for i in range(0, 4):
    for j in range(0, 4):
        print("# ", end="")
    print()

print()
print()
print()

for i in range(0, 4):
    for j in range(4-i):
        print("# ", end="")
    print()

for i in [8, 9, 12, 13, 14]:
    if i%5==0:
        print(i)
        break
else:
    print("Not found")