# Function :- Function code ka ek block hota hai jo kisi particular task ko perform karta hai.
# Simple words :- Ek baar function bana do, phir usko baar-baar use kar sakte ho.
# Function define kaise karein?
def hello():
    print("Hello Python")
# Function call karna
hello()

# Function mein parameters
def add(a, b):
    print(a + b)
add(10, 20)

# Parameter :- Function define karte time jo value receive hoti hai.
# Argument :- Function call karte time jo value pass karte hain.
# Function return karna
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
# return :- Function se result bahar bhejta hai.

# Single result return karna
def square(number):
    return number * number
result = square(5)
print(result)

# Multiple results return karna
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
x, y = calculate(20, 10)
print(x)
print(y)

# Function with no parameter
def message():
    print("Welcome")
message()

# Function with parameter
def message(name):
    print("Hello", name)
message("Shubham")

# FUNCTION AND METHOD
# Function :- Jo independently define hota hai.
def add(a, b):
    return a + b
print(add(10, 20))

# Method :- Jo kisi object ke saath use hota hai.
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# append() list ka method hai.
# Simple difference:
# Function -> independently call hota hai.
# Method   -> object ke saath call hota hai.


# POSITIONAL ARGUMENT :- Positional argument mein values ka order important hota hai.
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Shubham", 23)
# Yahan "Shubham" -> name
# aur 23 -> age

# KEYWORD ARGUMENT :-  Keyword argument mein parameter ka naam specify karke value pass karte hain.
def student(name, age):
    print("Name:", name)
    print("Age:", age)
    
student(age=23, name="Shubham")

# Yahan order important nahi hai
# kyunki parameter names diye hain.

# DEFAULT ARGUMENT :- Default argument mein parameter ko pehle se ek default value de dete hain.
def student(name, age=18):
    print("Name:", name)
    print("Age:", age)

student("Shubham")
# Yahan age nahi diya,
# isliye default value 18 use hogi.
# Default value ko change bhi kar sakte hain.
student("Shubham", 23)

# VARIABLE LENGTH ARGUMENT :-  Jab hume nahi pata hota ki kitne arguments pass honge, tab variable length argument use kar sakte hain.
# *args :- Multiple positional arguments receive karta hai.
def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)
# args ke andar values tuple ke form mein aati hain.

# *args ke saath loop
def numbers(*args):
    for number in args:
        print(number)

numbers(10, 20, 30, 40)

# **kwargs :- **kwargs multiple keyword arguments receive karta hai.
def student(**kwargs):
    print(kwargs)

student(name="Shubham", age=23, course="BCA")
# kwargs ke andar values dictionary ke form mein aati hain.

# **kwargs ko loop ke saath use karna
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

student(name="Shubham", age=23, course="BCA")


# PASS BY OBJECT REFERENCE :- Python mein arguments object reference ke through function ko pass hote hain.
# Mutable object ko function ke andar modify karne par
# original object bhi change ho sakta hai.

numbers = [10, 20, 30]
def change(numbers):
    numbers.append(40)
change(numbers)
print(numbers)
# Yahan original list change ho gayi
# kyunki list mutable object hai.

# Immutable object ka example:
number = 10
def change(number):
    number = 50
change(number)
print(number)
# Yahan original number change nahi hua
# kyunki integer immutable object hai.

# ANONYMOUS FUNCTION / LAMBDA :-  Anonymous function ko lambda function bhi kehte hain.  Is function ka normally koi naam nahi hota.
# Syntax:
# lambda arguments : expression
# Example:
square = lambda x: x * x
print(square(5))

# Do numbers mein bigger number find karna
bigger = lambda a, b: a if a > b else b
print(bigger(10, 20))

# Lambda function mein multiple arguments bhi ho sakte hain.
add = lambda a, b: a + b
print(add(10, 20))