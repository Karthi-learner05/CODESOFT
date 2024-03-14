def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if(y==0):
        print("Divide By Zero error")
    else:
        return x/y
print("\t\t------\tSIMPLE CALCULATOR\t-----")
print("1.Addition\t2.Substraction\t3.Multiplication\t4.Division\n")
while True:
    ch=int(input("Enter Your Choice = "))
    if ch in [1,2,3,4]:
        num1=float(input("First  Number    ="))
        num2=float(input("Second Number    ="))
        if ch==1:
            print("Addition       = ",add(num1,num2))
        elif ch==2:
            print("Substraction   = ",sub(num1,num2))
        elif ch==3:
            print("Multiplication = ",mul(num1,num2))
        elif ch==4:
            print("Division       = ",div(num1,num2))
        break
    else:
        print("Invalid Input...")
