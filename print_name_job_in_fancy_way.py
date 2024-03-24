# Purpose: ask the user to input their name, dream job, and dream city to work in. Print them in fancy way.

# Import necessary libraries: "pyfiglet" and "colorama".
import pyfiglet
from colorama import init, Fore

# Initialize "colorama" for colored text.
init(autoreset=True)

# Define functions for printing text in different colors: "print_green", "print_yellow", and "print_orange".
def print_green(text):
    print(Fore.GREEN + text)

def print_yellow(text):
    print(Fore.YELLOW + text)

def print_orange(text):
    print(Fore.LIGHTRED_EX + text)

# Prompt the user to enter their name, dream job, and dream city.

print_green("Please enter your name: ")
name = input()

print_yellow("Please enter your dream job: ")
dream_job = input()

print_orange("Please enter your dream city to work in: ")
dream_city = input()

# Use "pyfiglet" to format the entered name, dream job, and dream city.
print_green(pyfiglet.figlet_format(name))
print_yellow(pyfiglet.figlet_format(dream_job))
print_orange(pyfiglet.figlet_format(dream_city))

# Print a message wishing the user good luck with their dream in blue color
print("\033[94m]" + f"Good luck, {name}! You can do it! You will be a/an {dream_job} in {dream_city} in the future! Claim it! ")