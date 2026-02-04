# Task: Write program to convert temperature from Celsius to Fahrenheit


# Prompt user to enter a temperature in Celsius
celsius = float(input("Enter temperature in Celsius:"))

# Convert the Celsius temperature to Fahrenheit using the formula
fahrenheit = (celsius * 9 / 5) + 32
# Display converted temperature
print(f"{celsius}C is equal to {fahrenheit}F")


# Task: Create a program that calculates simple interest


# Prompt user enters principal amount
principal = float(input("Enter principal amount"))

# Prompt user enters annual interest rate(percentage)
rate = float(input("Enter annual interest rate (%):"))
# Prompt user enters time period(years)
time = float(input("Enter time period in years:"))
# Calculates simple interest using formula
interest = (principal * rate * time) / 100
# Display calculated interest
print(f"Simple interest is:{interest}")


# Task: Create a program to calculate area of rectangle.

# Prompt user to enter rectangle length
length = float(input("Enter the length of the rectangle:"))
# Prompt user to enter rectangle width
width = float(input("Enter width of rectangle"))
# Calculate the area using formula: length times width

# Display calculated area
