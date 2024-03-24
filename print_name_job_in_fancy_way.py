# Purpose: ask the user to input their name, dream job, and dream city to work in. Print them in fancy way.

# Import necessary libraries: "pyfiglet" and "colorama".
import pyfiglet
from colorama import init, Fore

# Initialize "colorama" for colored text.
init(autoreset=True)

# Define functions for printing text in different colors: "print_green", "print_yellow", and "print_orange".
def print_green(text):
    print(Fore.Green + text)
def print_yellow(text):
    print(Fore.Yellow + text)
def print_orangen(text):
    print(Fore.LIGHTRED_EX + text)

# Prompt the user to enter their name, dream job, and dream city.

print_green = ("Please enter your name: ")
name = input ()

print_yellow = ("Please enter your dream job: ")
dream_job = input()

print_orange = ("Please enter your dream city to work in: ")
dream_city = input()

# Use "pyfiglet" to format the entered name, dream job, and dream city.
formatted_name = pyfiglet.figlet_format(name)
formatted_dream_job = pyfiglet.figlet_format(dream_job)
formatted_dream_city = pyfiglet.figlet_format(dream_city)

# Print the formatted text.
print_name(formatted_name)
print_dream_job(formatted_dream_job)
print_dream_city(formatted_dream_city)

# Print a message wishing the user good luck with their dream.