from bisect import *

l=[10, 20, 30, 40, 50, 60, 70, 90]

insort(l, 25)
insort_left(l, 90)
insort_right(l, 90)
print(l)



print(bisect(l, 40))
print(bisect_left(l, 40))
print(bisect_right(l, 40))