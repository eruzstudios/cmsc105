
# This program takes two numeric values as input from the user,
# uses a constant value, and performs a mathematical computation.

# Define a constant value
CONSTANT_VALUE = 10

# Prompt the user for two numeric values
value1 = float(input("25"))
value2 = float(input("Enter the second numeric value: "))

# Perform a mathematical computation using the constant and user inputs
result = value1 + value2 + CONSTANT_VALUE

# Display the result
print(f"The result of {value1} + {value2} + {CONSTANT_VALUE} is: {result}")