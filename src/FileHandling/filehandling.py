

f = open("data", 'r')

for i in f:
    print(i, end="")


with open("data", 'w') as f1:
    for i in range(5):
        f1.write("Pranesh gunner is a gooner\n")


with open("data", 'a') as f1:
    for i in range(5):
        f1.write("Meriiii Mangoooo\n")


with open("passport_photo.jpeg", 'rb') as f2:
    with open("my_photo.jpeg", 'wb') as f3:
        for i in f2:
            f3.write(i)


import sys

print(sys.version_info, sys.version)

print(sys.platform)

sys.exit("Done for the day, see you again tomorrow")
