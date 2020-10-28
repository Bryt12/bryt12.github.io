import numpy as np

A = np.array([[1,-1,-1],[1, 1, 0], [1, 1, -2]])
B = np.array([[-1, 0, 0], [0, 1, 0], [1, 3, 1]])
C = np.array([1, 2, 3])
D = np.array([-1, 1, 0])

print("a)")
print(A + B)

print("b)")
print(A - B)

print("c)")
print(C.dot(D.transpose()))

print("d)")
print(5 * C)

print("e)")
print(A.dot(B))

print("f)")
print(A.transpose().dot(B))

print("g)")
print(B.transpose().dot(A))

print("h)")
print(A)

print("i)")
print(C.transpose().dot(A))

print("j)")
print(B.transpose().dot(D))
