import numpy as np
from numpy import concatenate

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'i')
print(arr)

l = [1, 2, 3]
k = np.asarray(l)
print(l, k)
print(type(l), type(k))

a = np.linspace(0, 100, 101)
print(a)
print(type(a))


a = np.logspace(0, 5, 5)
print(a)
print(type(a))


a = np.arange(0, 101, 5)
print(a)
print(type(a))

a = np.zeros(5, int)
print(a)
print(type(a))

a = a+5
print(a)


array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
list_2d = array_2d.tolist()
print(list_2d)

arr1=[1, 2, 3]
arr2=[4, 5, 6]
print(arr1+arr2)

list_l=[1, 2, 3]
tuple_t=(4, 5, 6)
set_s={7, 8, 9}

print(np.asarray(list_l))
print(np.asarray(tuple_t))
print(np.asarray(list(set_s)))

array_1=np.array([1, 2, 3, 4, 5])

array_2=array_1.copy()

print(id(array_1), id(array_2))

array_1[1]=7

print(id(array_1), id(array_2))