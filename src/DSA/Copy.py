# Shallow copy and Deep copy

import copy
l = [10, 20, 30, 40, 50, 60]

l1 = copy.copy(l)

"""
Shallow Copy
"""

l1[1]=1000
print(id(l1))
print(id(l))

print(l, l1)


print(id(l[0]))
print(id(l1[0]))

"""
Deep copy
"""

l2 = copy.deepcopy(l)
print(l, l2)