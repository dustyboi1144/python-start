print("check ODD - EVEN")
def posneg(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "zero"
num=int(input("Enter a number"))
if num%2==0:
    print("even and "+ posneg(num))
else:
    print("odd and "+posneg(num))
