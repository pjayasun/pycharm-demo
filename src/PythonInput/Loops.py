i = 1

while i <= 5:
    print("Pranesh ", end="")
    j = 1
    while j <= 5:
        print("Jayasundar ", end="")
        j += 1
    j = 1
    i += 1
    print()

# For loop

x = [1, 2, 3, 4, 10, 11, 12, 13]

for i in x:
    print(i)

for i in range(1, 11):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(21, 0, -2):
    print(i)

for _, i in enumerate(x):
    print(_, i)