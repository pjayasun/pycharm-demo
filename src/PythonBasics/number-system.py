from itertools import zip_longest

print(bin(25)[2:])

print(oct(25))

print(hex(25))

num=25

l=[]
while(num>0):
    rem=num%2
    num=num//2
    l.append(rem)

l.reverse()
print(l)

print(~14)

print()

a=5
print(a<<1)
print(a<<2)
print(a<<3)
print(a<<4)
print(a<<5)

b=100
print(b>>1)
print(b>>2)
print(b>>3)
print(b>>4)
print(b>>5)