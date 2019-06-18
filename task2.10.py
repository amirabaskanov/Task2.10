#     In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n!=1×2×…×n
# For the given integer n
# calculate the value n!. Don't use math module in this exercise.

number = int(input('Write your number:'))
result = 0
for a in range (1, number+1):
    x = 1
    for y in range (1, a+1):
        x *= y
    result += x
print (result)
