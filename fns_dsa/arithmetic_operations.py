# def perform_operation(float(num1), float(num2)):

#     num1=float(input("input the first number: " ))
#     num2=float(input("input the second number: " ))
#     operation = input("Enter 'add', 'subtract', 'multiply', or 'divide': " )

#     if operation == "add":
#         num3=num1+num2
#         print (f"{num1} + {num2} = {num3}")

#     elif operation == "subtract":
#         num3 = num1-num2
#         print(f"{num1} - {num2} = {num3}")

#     elif operation == "multiply":
#         num3 = num1*num2
#         print(f"{num1} * {num2} = {num3}")

#     elif operation == "divide":
#         num3 = num1/num2

#         if num2 == 0:
#             print ("cannot perform division at this time")

#     else:
#         print ("input either 'add', 'subtract', 'multiply', or 'divide'.")

# code block 2

# num1=float(input("input the first number: " ))
# num2=float(input("input the second number: " ))
# operation = input("Enter 'add', 'subtract', 'multiply', or 'divide': " )

# def perform_operation(num1, num2, operation):

#     if operation == "add":
#         num3=num1+num2
#         # print (f"{num1} + {num2} = {num3}")
#         return f"{num1} + {num2} = {num3}"
        
#     elif operation == "subtract":
#         num3 = num1-num2
#         # print(f"{num1} - {num2} = {num3}")
#         return f"{num1} - {num2} = {num3}"
        
#     elif operation == "multiply":
#         num3 = num1*num2
#         print(f"{num1} * {num2} = {num3}")
#         return f"{num1} * {num2} = {num3}"

#     elif operation == "divide":
#         if num2 == 0:
#             # print ("cannot perform division at this time")
#             return ("cannot perform division at this time")

#         else:
#             num3 = num1/num2
#             # print(f"{num1} / {num2} = {num3}")
#             return f"{num1} / {num2} = {num3}"

#     else:
#         return ("input either 'add', 'subtract', 'multiply', or 'divide'.")


# perform_operation(num1, num2, operation)


### code block 3
def perform_operation(num1, num2, operation):
    """
    Perform the specified arithmetic operation and return the result as a formatted string.
    """
    if operation == "add":
        num3 = num1 + num2
        return f"{num1} + {num2} = {num3}"

    elif operation == "subtract":
        num3 = num1 - num2
        return f"{num1} - {num2} = {num3}"

    elif operation == "multiply":
        num3 = num1 * num2
        return f"{num1} * {num2} = {num3}"

    elif operation == "divide":
        if num2 == 0:
            return "Cannot perform division at this time"
        else:
            num3 = num1 / num2
            return f"{num1} / {num2} = {num3}"

    else:
        return "Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."


# Main program
if __name__ == "__main__":
    num1 = float(input("Input the first number: "))
    num2 = float(input("Input the second number: "))
    operation = input("Enter 'add', 'subtract', 'multiply', or 'divide': ")

    # Call the function and handle the result
    result = perform_operation(num1, num2, operation)
    print(result)


