import math

# Ask the user for a number
number = float(input("Please enter a number: "))

# Calculate the square root, natural logarithm, and sine of the number
square_root = math.sqrt(number)
natural_log = math.log(number) if number > 0 else "undefined for non-positive numbers"
sine_value = math.sin(number)

# Display the calculated results
print(f"Square root of {number}: {square_root}")
print(f"Natural logarithm (log base e) of {number}: {natural_log}")
print(f"Sine of {number} (in radians): {sine_value}")
