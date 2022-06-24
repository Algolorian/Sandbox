import numpy as np

a = np.array([[1, 2, 3, 11, 22, 33], [4, 5, 6, 44, 55, 66]], dtype='int8')  # default dtype='int32'
# Data type example int16 int32 float16 float32
b = np.zeros((2, 3, 3))  # Initializes a 3d array of zeros 2 by 3 by 3
c = np.ones((2, 3, 3))  # Initializes a 3d array of zeros 2 by 3 by 3
d = np.full((2, 3), 5)  # Initializes a 2d array of 5's 2 by 3
e = np.random.rand(4, 2, 3)  # Initializes 3D array rand vals (0-1) 4 by 2 by 3
f = np.random.randint(-5, 5, size=(4, 2, 3))  # Initializes 3D array rand vals (-5 to 4, 5 is exclusive) 4 by 2 by 3
g = np.identity(5)  # Initializes 2D array identity matrix
h = np.repeat([d], 3, axis=0)  # Initializes repeated array

# Be careful when copying arrays
# if you alter a copy the original will be changed if arr2 = arr1
# Instead use "arr2 = arr1.copy" or "arr2 = arr1[:]"

# Mathematics
# You can use math operators directly on an array
# They will be used on every element within the array
# You can also use math operators between arrays
# a = [1, 2, 3, 4], b = [1, 0, 1, 5]
# a * 2 == [2, 4, 6, 8]
# a * b == [1, 0, 3, 20]
# Trig functions: np.sin(a) np.cos(a)
# np.min(a, axis=0) == [1   4]
# np.max(a, axis=0) == [33   66]
# np.sum(a, axis=0) == [72   180]
# a > 2 == [False, False, True, True]
# a[a > 2] == [3, 4]  # Returns all values in list greater than 2

# a = [[1, 3, 2, 4],
#      [4, 7, 3, 6]]
# np.any(a > 2, axis=0) == [True, True, True, True]
# np.all(a > 2, axis=0) == [False, True, False, True]
# np.any(a > 2, axis=1) == [True, True]
# np.all(a > 2, axis=1) == [False, True]

# a[[x1, x2, x3], [y1, y2, y3]]  # to index multiple

# Reorganizing arrays
# a = [[1, 2, 3, 4], [5, 6, 7, 8]]
# You can reshape an array to any dimension as long as the area is the same
# b = a.reshape((8, 1)) = [[1], [2], [3], [4], [5], [6], [7], [8]]
# b = a.reshape((4, 2)) = [[1, 2], [3, 4], [5, 6], [7, 8]]
# b = a.reshape((2, 2, 2)) = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# vstacks
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# np.vstack([a, b, a]) ==\
# [[1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [1, 2, 3, 4]]

# hstacks
# a = [[1, 2, 3, 4],
#      [1, 2, 3, 4]]
# b = [[5, 6, 7, 8],
#      [5, 6, 7, 8]]
# np.hstacks([a, b]) ==\
# [[1, 2, 3, 4], [5, 6, 7, 8],
#  [1, 2, 3, 4], [5, 6, 7, 8]]

# get text from file
filedata = np.genfromtxt('filename.txt', delimiter=',')  # Import data
filedata = filedata.astype('int32')  # Convert data to integer

# Array functions
print(a.ndim)  # Number of dimensions
print(a.shape)  # Dimension lengths
print(a.size)  # Length
print(a.itemsize)  # Bytes per item
print(a.nbytes)  # Total bytes for array

# Indexing functions
print(a[1, 1])  # To index 5
print(a[1, -1])  # To index 66
print(a[0, 1])  # To index 2
print(a[0, 0:-1:2])  # Format(start:stop:step) to index [ 1  3 22]
a[0, 0:-1:2] = 5  # Format(start:stop:step) to change [ 1  3 22] to [ 5 5 5]
print(a['#idx', :])  # Get a specific row
print(a[:, '#idx'])  # Get a specific column
# a = [1, 2, 3, 4]
# a[[0, 2]] == [1, 3]  # returns list of indices values
