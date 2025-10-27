operator = (input("Enter an operator(= - * /)"))
num1 = int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))

if operator =="+":
    print(num1+num2)
    print("The sum is", num1+num2)
elif operator =="-":
    print(num1-num2)
    print("The difference is", num1-num2)
elif operator =="*":
    print(num1*num2)
    print("The product is", num1*num2)
elif operator =="/":
    print(num1/num2)
    print("The quotient is", num1/num2)
else:
    print(f"{operator} not valid operator!!")