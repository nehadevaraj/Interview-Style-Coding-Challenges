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