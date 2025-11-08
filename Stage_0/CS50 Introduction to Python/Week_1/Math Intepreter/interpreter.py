text = input("Expression: ")
num1, operator, num2 = text.split(" ")
match operator:
    case "+":
        print(float(num1) + float(num2))
    case "-":
        print(float(num1) - float(num2))
    case "/":
        print(float(num1) / float(num2))
    case "*":
        print(float(num1) * float(num2))
    case _:
        print("Input a valid operator")
