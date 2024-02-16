import numpy as np

# Create a 2x3 array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Original array:")
print(arr)

# Accessing elements
print("\nAccessing elements:")
print("Element at (0, 0):", arr[0, 0])
print("Element at (1, 2):", arr[1, 2])

# Shape of the array
print("\nShape of the array:", arr.shape)

# Transpose of the array
print("\nTranspose of the array:")
print(arr.T)

# Sum of all elements
print("\nSum of all elements:", arr.sum())

# Element-wise operations
print("\nElement-wise operations:")
print("Square of the array:")
print(arr**2)
print("Element-wise square root of the array:")
print(np.sqrt(arr))
