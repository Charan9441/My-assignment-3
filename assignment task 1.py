def factorial(n):
    # Base case for recursion
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample number
number =int(input('Enter a number: '))
output = factorial(number)
print(f"The factorial of {number} is: {output}.")
