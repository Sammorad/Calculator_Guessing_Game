import pyinputplus as pyip
num1 = pyip.inputNum(prompt := "First Number: ")
operator = input("operator : ")
num2 = pyip.inputNum(prompt := "Second Number: ")
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