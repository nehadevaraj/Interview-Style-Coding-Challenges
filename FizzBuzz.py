# 1st example:
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

'''
for i in range(1, 101):
This line initializes a for loop that iterates over the numbers from 1 to 100 (inclusive). The loop variable i takes on values from 1 to 100 in each iteration.

if i % 3 == 0 and i % 5 == 0::
This is the first condition. It checks if the current value of i is divisible by both 3 and 5 without any remainder (i.e., it is a multiple of both 3 and 5). If this condition is true, it prints 'FizzBuzz'.

elif i % 3 == 0:
If the first condition is not met, this line is the second condition. It checks if the current value of i is divisible by 3 without any remainder. If true, it prints 'Fizz'.

elif i % 5 == 0:
If neither the first nor the second condition is met, this line is the third condition. It checks if the current value of i is divisible by 5 without any remainder. If true, it prints 'Buzz'.

else:
If none of the above conditions are true (i.e., i is not divisible by 3 or 5), this line is executed. It prints the current value of i.

In summary, this code is a FizzBuzz program. 
For each number from 1 to 100 (inclusive), it prints 'Fizz' if the number is divisible by 3, 'Buzz' if divisible by 5, 'FizzBuzz' if divisible by both 3 and 5, 
and the number itself if it doesn't meet any of these conditions. 
This is a classic programming exercise often used in interviews to test basic programming and logical reasoning skills.
'''
