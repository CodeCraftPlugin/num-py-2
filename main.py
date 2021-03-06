import numpy as ns

a = ns.array([1, "codecratft", 3])
print(a)
# Iterating Arrays.
for i in a:
    print(i)

# 2D array
ad = ns.array([[1, 2, 3], [4, 5, 6]])
print(ad)
for i in ad:
    print(i)

# We can iterate 2D arrays also.

# Numpy Array Join
arr1 = ns.array([[1, 2], [3, 8]])
arr2 = ns.array([[4, 5], [6, 7]])

arr = ns.concatenate((arr1, arr2), axis=1)
print(arr)

# Join two 2-D arrays along rows (axis=1):

# NumPy Array Slicing

# Slice elements from index 4 to the end of the array:

# Slice elements with step value:

# Perform Arithmetic Operations on Array

# Calculate square and sqrt of array elements:
