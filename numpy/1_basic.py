import numpy as np

import pandas

# print(np.arange(1,10,2))

# print(np.zeros((5,5)))


# print(np.linspace(0,20,10))



#solution

arr = np.zeros(10)
arr2 = np.ones(10)
arr3 = []
for i in range(0,10):
    arr3.append(5)


arr4 = np.arange(10,51)

arr5 = np.arange(0,9)
arr51 = arr5.reshape(3,3)

arr8 = np.eye(3)

arr9 = np.random.rand(1)

arr10 = np.random.randn(25)

arr11 = np.arange(0.01,1.01,0.01)

arr12 = np.linspace(0,1,20)


mat = np.arange(1,26).reshape(5,5)
print(mat)

arr13 = mat[2:,1: ]
arr14 = mat[3,-1]
arr15 = mat[:3,1].reshape(3,1)
arr16 = mat[-1,:]
arr17 = mat[-2:, :]
arr18 = mat.sum()
arr19 = mat.mean()
arr20 = mat.sum(axis=0)

print(arr20)