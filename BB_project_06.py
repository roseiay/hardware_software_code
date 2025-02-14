import os
import time

def clear_screen():
    """Clears the console screen for a cleaner look."""
    time.sleep(1)  # Small delay for readability
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_show_result():
    """Ask the user if they want to see their conversion result."""
    while True:
        choice = input("Would you like to see the result? (yes/no): ").strip().lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        print("Invalid input! Please enter 'yes' or 'no'.")

def binary_to_decimal(binary_str):
    """Converts a binary string to a decimal number."""
    decimal_value = int(binary_str, 2)
    if ask_show_result():
        print(f"Binary {binary_str} -> Decimal {decimal_value}")
    return decimal_value

def decimal_to_binary(decimal_num):
    """Converts a decimal number to a binary string."""
    binary_value = bin(decimal_num)[2:]
    if ask_show_result():
        print(f"Decimal {decimal_num} -> Binary {binary_value}")
    return binary_value

def decimal_to_hex(decimal_num):
    """Converts a decimal number to a hexadecimal string."""
    hex_value = hex(decimal_num)[2:].upper()
    if ask_show_result():
        print(f"Decimal {decimal_num} -> Hexadecimal {hex_value}")
    return hex_value

def hex_to_decimal(hex_str):
    """Converts a hexadecimal string to a decimal number."""
    decimal_value = int(hex_str, 16)
    if ask_show_result():
        print(f"Hexadecimal {hex_str} -> Decimal {decimal_value}")
    return decimal_value

def binary_to_hex(binary_str):
    """Converts a binary string to a hexadecimal string."""
    decimal_value = int(binary_str, 2)
    hex_value = hex(decimal_value)[2:].upper()
    if ask_show_result():
        print(f"Binary {binary_str} -> Hexadecimal {hex_value}")
    return hex_value

def hex_to_binary(hex_str):
    """Converts a hexadecimal string to a binary string."""
    decimal_value = int(hex_str, 16)
    binary_value = bin(decimal_value)[2:]
    if ask_show_result():
        print(f"Hexadecimal {hex_str} -> Binary {binary_value}")
    return binary_value

def decimal_to_octal(decimal_num):
    """Converts a decimal number to an octal string."""
    octal_value = oct(decimal_num)[2:]
    if ask_show_result():
        print(f"Decimal {decimal_num} -> Octal {octal_value}")
    return octal_value

def octal_to_decimal(octal_str):
    """Converts an octal string to a decimal number."""
    decimal_value = int(octal_str, 8)
    if ask_show_result():
        print(f"Octal {octal_str} -> Decimal {decimal_value}")
    return decimal_value

def binary_to_octal(binary_str):
    """Converts a binary string to an octal string."""
    decimal_value = int(binary_str, 2)
    octal_value = oct(decimal_value)[2:]
    if ask_show_result():
        print(f"Binary {binary_str} -> Octal {octal_value}")
    return octal_value

def validate_binary(binary_str):
    """Ensures the input consists only of 0s and 1s."""
    return all(char in '01' for char in binary_str)

def validate_decimal(decimal_str):
    """Ensures the input is a valid positive integer."""
    return decimal_str.isdigit()

def validate_hex(hex_str):
    """Ensures the input is a valid hexadecimal string."""
    return all(char in '0123456789ABCDEFabcdef' for char in hex_str)

def validate_octal(octal_str):
    """Ensures the input is a valid octal number (digits 0-7)."""
    return all(char in '01234567' for char in octal_str)

def main():
    """Runs the interactive number conversion program."""
    print("""
    ███████╗██╗     ██╗██████╗ 
    ██╔════╝██║     ██║██╔══██╗
    █████╗  ██║     ██║██████╔╝
    ██╔══╝  ██║     ██║██╔═══╝ 
    ██║     ███████╗██║██║     
    ╚═╝     ╚══════╝╚═╝╚═╝     

       Get ready to flip the world! 
    """)
    print("Welcome! Pick your weapon! It's time to convert numbers!")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Convert Binary to Decimal")
        print("2. Convert Decimal to Binary")
        print("3. Convert Decimal to Hexadecimal")
        print("4. Convert Hexadecimal to Decimal")
        print("5. Convert Binary to Hexadecimal")
        print("6. Convert Hexadecimal to Binary")
        print("7. Convert Decimal to Octal")
        print("8. Convert Octal to Decimal")
        print("9. Convert Binary to Octal")
        print("10. Exit")
        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            binary_input = input("Enter a binary number: ")
            if validate_binary(binary_input):
                binary_to_decimal(binary_input)
            else:
                print("Invalid binary number! Please enter only 0s and 1s.")

        elif choice == '2':
            decimal_input = input("Enter a decimal number: ")
            if validate_decimal(decimal_input):
                decimal_to_binary(int(decimal_input))
            else:
                print("Invalid decimal number! Please enter a valid positive integer.")

        elif choice == '3':
            decimal_input = input("Enter a decimal number: ")
            if validate_decimal(decimal_input):
                decimal_to_hex(int(decimal_input))
            else:
                print("Invalid decimal number! Please enter a valid positive integer.")

        elif choice == '4':
            hex_input = input("Enter a hexadecimal number: ").upper()
            if validate_hex(hex_input):
                hex_to_decimal(hex_input)
            else:
                print("Invalid hexadecimal number! Please enter valid hexadecimal characters (0-9, A-F).")

        elif choice == '5':
            binary_input = input("Enter a binary number: ")
            if validate_binary(binary_input):
                binary_to_hex(binary_input)
            else:
                print("Invalid binary number! Please enter only 0s and 1s.")

        elif choice == '6':
            hex_input = input("Enter a hexadecimal number: ").upper()
            if validate_hex(hex_input):
                hex_to_binary(hex_input)
            else:
                print("Invalid hexadecimal number! Please enter valid hexadecimal characters (0-9, A-F).")

        elif choice == '7':
            decimal_input = input("Enter a decimal number: ")
            if validate_decimal(decimal_input):
                decimal_to_octal(int(decimal_input))
            else:
                print("Invalid decimal number! Please enter a valid positive integer.")

        elif choice == '8':
            octal_input = input("Enter an octal number: ")
            if validate_octal(octal_input):
                octal_to_decimal(octal_input)
            else:
                print("Invalid octal number! Please enter only digits (0-7).")

        elif choice == '9':
            binary_input = input("Enter a binary number: ")
            if validate_binary(binary_input):
                binary_to_octal(binary_input)
            else:
                print("Invalid binary number! Please enter only 0s and 1s.")

        elif choice == '10':
            print("\nExiting the program... Awww man, no more flipping? Okay...")
            print("This project required approximately 2 to 4 Monsters...")
            print("And now my keyboard is jittery from all the caffeine.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 10.")

        clear_screen()

if __name__ == "__main__":
    main()
