num1 = float(input("Enter the first number: " ))

num2 = float(input("Enter the second number: " ))

operation = input("Choose the operation (+, -, *, /): " )

match operation:
    case "+":
        num3 = num1 + num2
        # print ("num1 + num2 = ", num3)
        # print ("The result is ", num3)
        print(f"The result is {result}")
        

    case "-":
        num3 = num1 - num2
        # print (num3)
        # print ("num1 - num2 = ", num3)
        # print ("The result is ", num3)
        print(f"The result is {result}")


    case "*":
        num3 = num1 * num2
        # print(num3)
        # print ("num1 * num2 = ", num3)
        # print ("The result is ", num3)
        print(f"The result is {result}")



    case "/":
        num3 = num1/num2
        # print(num3)
        # print ("num1 / num2 = ", num3)
        if num2 == 0:
            print ("Cannot divide by zero. ")
        else:
            # print ("The result is ", num3)
            print(f"The result is {result}")

        
