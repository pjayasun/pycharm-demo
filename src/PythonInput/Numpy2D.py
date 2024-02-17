import numpy as np

array1=np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(array1.ndim)
print(array1.shape)
print(array1.size)

array2=array1.reshape(-1)

print(array2.ndim)
print(array2.shape)
print(array2.size)
print(array2)

array3=array2.reshape(3, -1)
print(array3.ndim)
print(array3.shape)
print(array3.size)
print(array3)


lis=[[1, 2], [3, 4]]
tup=((5, 6), (8, 9))

matrix1=np.matrix(lis)
matrix2=np.matrix(tup)

print(matrix1)
print(matrix1.ndim)
print(matrix1.shape)
print(matrix1.min())

print(matrix2)
print(matrix2.ndim)
print(matrix2.shape)
print(matrix2.min())

matrix3=matrix2*matrix1
print(matrix1)
print(matrix2)
print(matrix3)