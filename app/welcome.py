# Python code to get user information

# Prompting the user for input
name = input("Enter your name: ")
age = input("Enter your age: ")
favorite_language = input("Enter your favorite programming language: ")

# Displaying the gathered information
print("\nHello, " + name + "!")
print("You are " + age + " years old.")
print("Your favorite programming language is " + favorite_language + ".")

# Calculate the year when the user will turn 100 years old
current_year = 2024  # Update this with the current year
years_to_100 = 100 - int(age)
year_of_100 = current_year + years_to_100

# Display the calculated information
print("You will turn 100 years old in the year " + str(year_of_100) + ".")


# Additional message
print("\nKeep coding and have a great day!")
