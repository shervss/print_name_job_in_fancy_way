# Purpose: ask the user to input their name, dream job, and dream city to work in. Print them in fancy way.

# Import necessary libraries: "pyfiglet" and "colorama".
import pyfiglet
from colorama import init, Fore

# Initialize "colorama" for colored text.
init(autoreset=True)

# Prompt the user to enter their name, dream job, and dream city.
name = input("Please enter your name: ")
dream_job = input("Please enter your dream job: ")
dream_city = input("Please enter your dream city to work in: ")

# Initialize "colorama" for colored text.
# Define functions for printing text in different colors: "print_green", "print_yellow", and "print_orange".
# Print the prompts in the desired colors using the defined functions.
# Use "pyfiglet" to format the entered name, dream job, and dream city.
# Print the formatted text.
# Print a message wishing the user good luck with their dream.