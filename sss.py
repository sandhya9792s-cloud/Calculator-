num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
print("1. Addition")
print("2. Subtracation")
print("3. Multipulication")
print("4. Division")
choice=input("enter your choice(1/2/3/4):")
if choice=="1":
    print("result=",num1+num2)
elif choice=="2":
    print("result=",num1-num2)
elif choice=="3":
    print("result=",num1*num2)
elif choice=="4":
    if num2 !=0:
        print("result=",num1/num2)
    else:
        print("cannot divide by zero")
else:
    print("invalid choice")
