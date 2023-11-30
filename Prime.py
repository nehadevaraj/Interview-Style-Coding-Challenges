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

'''
def is_prime(number):
This line defines a function named is_prime that takes an integer number as its parameter.
# 0 and 1 are not prime numbers:
This is a comment explaining that 0 and 1 are not considered prime numbers.

if number < 2:
This line checks if the input number is less than 2. If it is, the function immediately returns False, indicating that numbers less than 2 are not prime.

# Check for factors from 2 to the square root of the number:
This is a comment explaining the next block of code, which is a loop to check for factors.

for i in range(2, int(number**0.5) + 1):
This line starts a for loop that iterates over i from 2 to the square root of the input number. The + 1 is used to include the square root itself in the range.

if number % i == 0:
Inside the loop, this line checks if the input number is divisible evenly by i. If it is, it means the number has a factor other than 1 and itself, 
so the function returns False.

return False # It has a factor other than 1 and itself:
If the loop completes without finding any factors, the function returns True at the end, indicating that the number is prime.

return True # It's a prime number:
This line is reached if the input number is greater than or equal to 2 and has no factors other than 1 and itself. It returns True, indicating that the number is prime.

number_to_check = 13:
This line sets a variable number_to_check to the value 13. This is the number that will be checked for primality.

if is_prime(number_to_check):
This line checks if the function is_prime returns True for the given number_to_check.

print(f"{number_to_check} is a prime number."):
If the number is prime, this line prints a message indicating that the number is a prime number.

else:
If the number is not prime, this line is executed.

print(f"{number_to_check} is not a prime number."):
This line prints a message indicating that the number is not a prime number.

In summary, the script defines a function to check if a given number is prime and demonstrates its usage by checking whether the number 13 is prime or not. 
The function works by checking for factors from 2 to the square root of the number, making it an efficient approach for primality testing.
'''
