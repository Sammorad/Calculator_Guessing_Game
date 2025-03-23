def calculator():
    """Here is a claculator that can perform any of addition, subtraction, multiplication or division"""
    while True:
        details = input("Type 'exit' to quit or input details: ")
        if details == "exit":
            break
        """lets take care of invalid inputs"""
        try: 
            num = details.split(" ")
            num[0] = int(num[0])
            num[2] = int(num[2])

        except:
            print("invalid input correct format : A + B")
        else:
            
            if num[1] == "+": 
                print(num[0] + num[2])
            elif num[1] == "-":
                print(num[0] -num[2])
            elif num[1] == "*":
                print(num[0] * num[2])
            elif num[1] == "/":
                """lets take care of zerp division error"""
                try:
                    print(num[0]/num[2])
                except ZeroDivisionError:
                    print("You cannot divide by zero")
                else:
                    print(num[0]/num[2])
            
calculator()  

