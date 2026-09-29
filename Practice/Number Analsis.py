# User se ek number lo aur check karo:
# Positive, negative ya zero
# Even ya odd
# 5 se divisible hai ya nahi
# Use: input(), int(), %, if-elif-else, logical operators

Number=int(input("Enter a Number :- "))

if Number > 0:
    print(f"{Number} is Positive")
elif Number < 0:
    print(f"{Number} is Negative")
else:
    print(f"{Number} is Zero")

if Number%2==0:
    print(f"{Number} is Even")
else:
    print(f"{Number} is Odd")

if Number%5==0:
    print(f"{Number} is Divisible by 5")
else:
    print(f"{Number} is Not Divisible by 5")