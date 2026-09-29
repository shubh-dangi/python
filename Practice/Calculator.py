# User se 2 numbers aur ek operator (+, -, *, /) lo aur result print karo.
# Invalid operator par "Invalid Operator" print karo.
# Use: input(), type conversion, match-case, arithmetic operators

Num1=int(input("Enter No 1 :- "))
Num2=int(input("Enter No 2 :- "))
icon=input("Enter What You Want :- ")
match icon:
    case "+": 
        print("Sum :- ",Num1+Num2)
    case "-":
        print("Minus :- ",Num1-Num2)
    case "*":
        print("MUltiplication :- ",Num1*Num2)
    case "/":
        print("Divide :- ",Num1/Num2)
    case _:
        print("Invalid Icon Entered")
