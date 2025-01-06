num1 = float(input("Enter the first number: " ))

num2 = float(input("Enter the second number: " ))

operation = input("Choose the operation (+, -, *, /): " )

match operation:
    case "+":
        num3 = num1 + num2
        print ("num1 + num2 = ", num3)

    case "-":
        num3 = num1 - num2
        # print (num3)
        print ("num1 - num2 = ", num3)


    case "*":
        num3 = num1 * num2
        # print(num3)
        print ("num1 * num2 = ", num3)


    case "/":
        num3 = num1/num2
        # print(num3)
        print ("num1 / num2 = ", num3)

        
