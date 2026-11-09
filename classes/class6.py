num1 = int(input("Enter first number: "))
operator = input("Choose any operator: ")
num2 = int(input("Enter the second number: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
    
else:
    print("ERROR....")