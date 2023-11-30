# 4th example:
def is_prime(number):
    # 0 and 1 are not prime numbers
    if number < 2:
        return False
    
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # It has a factor other than 1 and itself
    
    return True  # It's a prime number
'''
# Example usage:
# Assuming you want to check if 17 is a prime number
number_to_check = 13
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")
'''