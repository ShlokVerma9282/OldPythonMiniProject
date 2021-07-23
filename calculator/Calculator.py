loop=False
while not loop:
    def calc(num1,symbol,num2):
        result=0
        if symbol=="+":
            result=num1+num2
            print(f"The Result is: {num1}"+" + "+f"{num2}"+" = "+f"{result}\n")
        elif symbol=="-":
            result=num1-num2
            print(f"The Result is: {num1}"+" - "+f"{num2}"+" = "+f"{result}\n")
        elif symbol=="*":
            result=num1+num2
            print(f"The Result is: {num1}"+" * "+f"{num2}"+" = "+f"{result}\n")
        elif symbol=="/":
            result=num1/num2
            print(f"The Result is: {num1}"+" / "+f"{num2}"+" = "+f"{result}\n")
        else:
            print("Invalid")

    num1=int(input("What is your first number:\n"))
    symbol=str(input("You want to do:\n+\n-\n*\n/\n"))
    num2=int(input("What is your second number:\n"))
    calc(num1,symbol,num2)
    last=input("Do you want to continue y or n:\n")
    if last=="n":
      loop=True
    elif last=="y":
      loop=False
    else:
        print("Error")
        loop=True
