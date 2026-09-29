# Conditional Statements :- Agar condition true hai → ye code chalao, warna doosra code chalao.
# Python mein mainly :- if , if-else , if-elif-else , Nested if , Ternary operator , match-case.

# 1. if Statement :- Sabse basic condition.
# Syntax :- 
# if condition:
    # code

age=34    
if age >= 18:
    print("You are eligible")

# 2. if-else :- Jab condition ke True aur False dono cases handle karne ho.

# Syntax :- 
# if condition:
    # true
# else:
    # false
    
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 3. if-elif-else :- Jab multiple conditions check karni ho.
# Syntax :- 
# if condition1:
    # code
# elif condition2:
    # code
# elif condition3:
    # code
# else:
    # code

marks = 75
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
# Note :- Python conditions ko upar se neeche check karta hai.

# 4. Multiple if vs if-elif :- Ye difference important hai.
age = 20
if age >= 18:
    print("Adult")
if age >= 20:
    print("20 or above")

age = 20
if age >= 18:
    print("Adult")
elif age >= 20:
    print("20 or above")
# Second condition check nahi hogi because first condition already True hai.

# 5. Nested if :- if ke andar if = nested if.
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible")

# 6. Nested if-else :-
age = 20
citizen = False
if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Not a citizen")
else:
    print("Under age")

# 7. Ternary Operator :- Simple if-else ko one line mein likhne ka short method.
age = 20
if age >= 18:
    result = "Adult"
else:
    result = "Minor"

print(result)

# Ternary :- 
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)
# Formula :- value_if_true if condition else value_if_fals 

# 8. match-case :- Python mein multiple fixed values ke according decision lene ke liye match-case use kar sakte hain.
day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid")

# 9. match-case with String :-
color = "red"
match color:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Wait")
    case _:
        print("Unknown")

# 10. Conditions mein Logical Operators :- Conditions ke saath and, or, not bhi use kar sakte ho. 
# and :- Dono conditions True honi chahiye.
age = 20
if age >= 18 and age <= 60:
    print("Valid age")

# or :- Koi ek condition True ho to chalega.
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")

# not :- Condition ka result reverse karta hai.
login = False
if not login:
    print("Please login")

# 11. Conditions with Comparison Operators :- Mostly conditions mein comparison operators use honge:
# a == b , a != b , a > b , a < b , a >= b , a <= b
marks = 80
if marks >= 50:
    print("Pass")
    
# 12. Truthy & Falsy Values :-Python mein kuch values condition mein automatically False treat hoti hain.
name = ""
if name:
    print("Name exists")
else:
    print("Name is empty")

# Non-empty string generally True hoti hai:
name = "Shubham"
if name:
    print("Name exists")