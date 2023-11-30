# 2nd example:
import numpy as np

def cov_to_corr(covariance_matrix):
    # Calculate the standard deviations for each variable (sqrt of the diagonal elements of the covariance matrix)
    std_devs = np.sqrt(np.diag(covariance_matrix))
    
    # Calculate the outer product of standard deviations
    std_devs_outer = np.outer(std_devs, std_devs)
    
    # Calculate the correlation matrix
    correlation_matrix = covariance_matrix / std_devs_outer
    
    return correlation_matrix
'''
# Example usage:
# Assuming you have a covariance matrix cov_matrix
cov_matrix = np.array(
    [[1.0, 0.5, 0.2],
    [0.5, 2.0, 0.8],
    [0.2, 0.8, 0.5]])

correlation_matrix = cov_to_corr(cov_matrix)
print("Correlation Matrix:")
print(correlation_matrix)
''' 

'''
import numpy as np:
This line imports the NumPy library and gives it the alias np. NumPy is a powerful library for numerical operations in Python.

def cov_to_corr(covariance_matrix):
This line defines a function named cov_to_corr that takes a covariance matrix as input.

std_devs = np.sqrt(np.diag(covariance_matrix)):
This line calculates the standard deviations for each variable. It uses NumPy's sqrt function to take the square root of the diagonal elements 
of the covariance matrix using np.diag.

std_devs_outer = np.outer(std_devs, std_devs):
This line calculates the outer product of the standard deviations. It uses NumPy's outer function to compute the matrix resulting from the multiplication 
of each element in std_devs with each element in its transpose.

correlation_matrix = covariance_matrix / std_devs_outer:
This line calculates the correlation matrix by dividing each element of the covariance matrix by the corresponding element in std_devs_outer. 
This step is part of the process of converting a covariance matrix to a correlation matrix.

return correlation_matrix:
The function returns the calculated correlation matrix.

cov_matrix = np.array([[1.0, 0.5, 0.2], [0.5, 2.0, 0.8], [0.2, 0.8, 0.5]]):
This line creates a 3x3 covariance matrix named cov_matrix as an example. You can replace this with your own covariance matrix.

correlation_matrix = cov_to_corr(cov_matrix):
This line calls the cov_to_corr function with the cov_matrix as an argument, calculating the correlation matrix.

print("Correlation Matrix:"):
This line prints a header indicating that the following output is the correlation matrix.

print(correlation_matrix):
This line prints the calculated correlation matrix to the console.

In summary, the script defines a function to convert a covariance matrix to a correlation matrix and demonstrates its usage with an example covariance matrix. 
The correlation matrix is printed to the console. This process is common in statistics and data analysis to normalize the scale of variables and make them comparable.
'''
