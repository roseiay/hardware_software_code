def celsius_to_fahr(temp):
    # Convert Celsius temperature to Fahrenheit using the formula.
    temp = 9/5 * temp + 32
    # Return the result as a formatted string.
    return "The freezing point of water in Fahrenheit is: {}".format(temp)

def kelvins_to_celsius(temp_kelvins):
    # Convert Kelvin temperature to Celsius using the formula.
    temp = temp_kelvins - 273.15
    # Return the result as a formatted string.
    return "The absolute freezing point of water in Celsius is: {}".format(temp)

def main():
    # Define the Celsius temperature for freezing point.
    temp = 0  # 0 degrees Celsius
    freezing_point = celsius_to_fahr(temp)
    print(freezing_point)
    absolute_zero = kelvins_to_celsius(temp)
   
    print(absolute_zero)

if __name__ == "__main__":
    main()