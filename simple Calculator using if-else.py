operator=input("ENTER AN OPERATOR(+,-,*,/): ")
num1=float(input("ENTER NUMBER1 : "))
num2=float(input("ENTER NUMBER2 : "))

if operator=="+":
    result=num1+num2
    print(round(result))
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1-num2
    print(result)
elif operator== "/":
    result=num1-num2
    print(result)
elif operator=="":
    print("ENTER A VALID OPERATOR")
