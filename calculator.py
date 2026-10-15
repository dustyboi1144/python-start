print("CALCULATOR")
num1=float(input("enter the first number: "))
operator=input("enter the operator (for eg: +,-,%,/,*,**): ").strip()
num2=float(input("enter the second number: "))
if(operator=='+'):
    print(num1+num2)
elif(operator=='-'):
    print(num1-num2)
elif(operator=='%'):
    print(num1%num2)
elif(operator=='/'):
    if(num2==0):
        print("invalid(cannot divide by 0)")
    else:
        print(num1/num2)
elif(operator=='*'):
    print(num1*num2)
elif(operator=='**'):
    print(num1**num2)
else:
    print("invalid inputs")
