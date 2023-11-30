# 3rd example:
import numpy as np

def inverse_2x2(matrix):
    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]
    
    determinant = a*d - b*c
    
    if determinant == 0:
        raise ValueError("The matrix is singular, and its inverse does not exist.")
    
    inverse_matrix = np.array(
        [[d, -b],
        [-c, a]]) / determinant
    
    return inverse_matrix
'''
# Example usage:
# Assuming you have a 2x2 matrix A
A = np.array(
    [[2, 3],
    [4, 5]])

inverse_A = inverse_2x2(A)
print("Inverse of A:")
print(inverse_A)
'''

'''
import numpy as np:
This line imports the NumPy library and gives it the alias np. NumPy is a powerful library for numerical operations in Python.

def inverse_2x2(matrix):
This line defines a function named inverse_2x2 that takes a 2x2 matrix as input.

a, b = matrix[0, 0], matrix[0, 1]:
These lines extract the elements of the input matrix using array indexing. a and b represent the elements in the first row of the first column and 
first row of the second column, respectively.

c, d = matrix[1, 0], matrix[1, 1]:
Similarly, these lines extract the elements in the second row of the first column and second row of the second column, assigning them to variables c and d.

determinant = a * d - b * c:
This line calculates the determinant of the 2x2 matrix using the formula ad−bcad−bc. The determinant is a crucial value in determining whether the matrix has an inverse.

if determinant == 0:
This line checks if the determinant is zero. If the determinant is zero, the matrix is singular, and its inverse does not exist. In this case, a ValueError is raised.

raise ValueError("The matrix is singular, and its inverse does not exist."):
If the determinant is zero, this line raises a ValueError with a message indicating that the matrix is singular and its inverse does not exist.

inverse_matrix = np.array([[d, -b], [-c, a]]) / determinant:
This line calculates the elements of the inverse matrix using the formula 1determinant×[d−b−ca]determinant1×[d−c−ba].

return inverse_matrix:
The function returns the calculated inverse matrix.

A = np.array([[2, 3], [4, 5]]):
This line creates a 2x2 matrix named A as an example. You can replace this with your own 2x2 matrix.

inverse_A = inverse_2x2(A):
This line calls the inverse_2x2 function with the matrix A as an argument, calculating the inverse matrix.

print("Inverse of A:"):
This line prints a header indicating that the following output is the inverse of matrix A.

print(inverse_A):
This line prints the calculated inverse matrix to the console.

In summary, the script defines a function to calculate the inverse of a 2x2 matrix and demonstrates its usage with an example matrix. 
The inverse matrix is printed to the console if it exists; otherwise, a ValueError is raised. 
Calculating the inverse of a matrix is a fundamental operation in linear algebra and is often used in various fields, including computer graphics, optimization, 
and statistics.
'''
