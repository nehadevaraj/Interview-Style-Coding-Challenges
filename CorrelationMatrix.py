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