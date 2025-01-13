
#
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)

#
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

# scoping the function parameter
global fahrenheit
global celsius

#
def convert_to_celsius(fahrenheit):
   # global fahrenheit  # /fix "fahrenheit" is assigned before global declaration
    c_t_c = FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit
    return c_t_c # ie 0.0°C is 32.0°F

#
def convert_to_farenheit(celsius):
    c_t_f = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius
    return c_t_f


# alternative to error message
def error_function():
    print("Error- invalid tempeorature please enter a numeric value")

    temp_unit = input("Enter a temperature unit(c/f): ")

    temp_value = float(input("Enter temperature value : " ))


#
temp_unit = input("Enter a temperature unit(c/f): ")

temp_value = float(input("Enter temperature value : " ))


#
if temp_unit == "c":
    # temp_value = fahrenheit # this is meant to be equatiing the farenheit in the function
    fahrenheit = temp_value
    c_t_c=convert_to_celsius(fahrenheit) # if this doesnt work, try convert_to_celsius(fahrenheit=temp_value)
    print(c_t_c) 

    # to continue ask if the person will like to continue to input (i think to achieve this, 
    # the enclosing if statement should be a function and i should also try and leverage packages and modules for personal practice)
        # ask=input("would you like to continue? (yes/no): ")

        # if ask == "yes":
        
    


elif temp_unit == "f":
    celsius = temp_value
    c_t_f=convert_to_farenheit(celsius) # if this doesnt work, try convert_to_celsius(celsius=temp_value)
    print(c_t_f)
     

else:
    # print ("Error- invalid tempeorature please enter a numeric value")
    error_function()