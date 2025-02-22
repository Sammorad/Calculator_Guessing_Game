num1 = input("First Number: ")
operator = input("operator : ")
num2 = input("Second Number ")
num1 = float(num1) # first number 
num2 = float(num2) # second number 
if operator == "+": 
    print(num1 + num2)
elif operator == "-":
    print(num1 -num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1/num2)
else: 
    print("check operator")