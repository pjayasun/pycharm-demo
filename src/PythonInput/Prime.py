from math import ceil

x = int(input("Enter a number"))

for i in range(2, ceil(x**0.5)+1):
    if x % i == 0:
        print("Not prime")
        break
else:
    print("Prime")