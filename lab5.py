# INF 102 - Project 05
# Maker: Barry

import time  # Importing time module to use time.sleep()

def print_banner():
    print("=" * 50)
    print(" " * 10 + "WELCOME TO THE ADDITION PROGRAMMING")
    print("=" * 50)

def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def add_numbers():
    while True:
        print("\nLet's add two numbers!")
        num1 = get_valid_number("Enter the first whole number: ")
        num2 = get_valid_number("Enter the second whole number: ")
        
        result = num1 + num2
        print(f"\nThe sum of {num1} and {num2} is: {result}")

        while True:
            exit_program = input("\nDo you want to add more numbers? (yes/no): ").strip().lower()
            if exit_program in ['yes', 'no']:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if exit_program == 'no':
            print("\nExiting the program. Thank you for using it!")
            time.sleep(1)
            break

print_banner()
add_numbers()
