
# #
# global FAHRENHEIT_TO_CELSIUS_FACTOR
# FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)

# #
# global CELSIUS_TO_FAHRENHEIT_FACTOR
# CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

# # scoping the function parameter
# global fahrenheit
# global celsius
# # global FAHRENHEIT_TO_CELSIUS_FACTOR # error
# # global CELSIUS_TO_FAHRENHEIT_FACTOR # error

# #
# def convert_to_celsius(fahrenheit):
#    # global fahrenheit  # /fix "fahrenheit" is assigned before global declaration
#     c_t_c = FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit
#     return c_t_c # ie 0.0°C is 32.0°F

# #
# def convert_to_farenheit(celsius):
#     c_t_f = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius
#     return c_t_f


# # alternative to error message
# def error_function():
#     print("Error- invalid tempeorature please enter a numeric value")

#     temp_unit = input("Enter a temperature unit(c/f): ")

#     temp_value = float(input("Enter temperature value : " ))


# #
# temp_unit = input("Enter a temperature unit(c/f): ")

# temp_value = float(input("Enter temperature value : " ))


# #
# if temp_unit == "c":
#     # temp_value = fahrenheit # this is meant to be equatiing the farenheit in the function
#     fahrenheit = temp_value
#     c_t_c=convert_to_celsius(fahrenheit) # if this doesnt work, try convert_to_celsius(fahrenheit=temp_value)
#     print(c_t_c) 

#     # to continue ask if the person will like to continue to input (i think to achieve this, 
#     # the enclosing if statement should be a function and i should also try and leverage packages and modules for personal practice)
#         # ask=input("would you like to continue? (yes/no): ")

#         # if ask == "yes":
        
    


# elif temp_unit == "f":
#     celsius = temp_value
#     c_t_f=convert_to_farenheit(celsius) # if this doesnt work, try convert_to_celsius(celsius=temp_value)
#     print(c_t_f)
     

# else:
#     # print ("Error- invalid tempeorature please enter a numeric value")
#     error_function()

#---------------------------------------------------------------------------------------------------------------------------------------------------
# APPROACH 2
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to interact with the user and perform temperature conversions.
    """
    print("Temperature Conversion Tool")
    print("Enter a temperature followed by its unit (C for Celsius, F for Fahrenheit).")
    
    try:
        # Prompt user for temperature and unit
        temperature_input = input("Enter the temperature (e.g., 100C or 212F): ").strip().upper()
        if not temperature_input[:-1].replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temperature_input[:-1])  # Extract numeric value
        unit = temperature_input[-1]  # Extract the unit (C or F)

        if unit == 'C':  # Convert Celsius to Fahrenheit
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result:.2f}°F.")
        elif unit == 'F':  # Convert Fahrenheit to Celsius
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result:.2f}°C.")
        else:  # Invalid unit
            raise ValueError("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
