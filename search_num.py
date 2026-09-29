# Ek list banao numbers = [10, 25, 30, 45, 50, 60]
# User se number lo aur search karo.
# Mil gaya → "Number Found"
# Nahi mila → "Number Not Found"
# Use: list, input(), for, if, break, for-else

numbers=[10,23,34,56,74,32]
num=int(input("Enter Number to Find :- "))

for i in numbers:
    if i == num:
        print("Number Found !")
        break
else:
    print("Number Not Found")