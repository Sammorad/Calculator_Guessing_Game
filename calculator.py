"""Here is a claculator that can perform any of addition, subtraction, multiplication or division"""
try:
    Calculate = input("Display input: ")
    num = Calculate.split(" ")
    num[0] = int(num[0])
    num[2] = int(num[2])
    if num[1] == "+": 
        print(num[0] + num[2])
    elif num[1] == "-":
        print(num[0] -num[2])
    elif num[1] == "*":
        print(num[0] * num[2])
    elif num[1] == "/":
        print(num[0]/num[2])
    else: 
        print("check operator")
except: 
    print("invalid input, correct format: A + B")
print(num)