# Exception Handling :-Exception ek runtime error hota hai jo program ke execution ke time par aata hai. Exception ki wajah se program normally stop ho sakta hai. Exception Handling ka use error ko handle karne ke liye hota hai.

# Example without Exception Handling :-
a = 10
b = 0
print(a / b)    # Ye ZeroDivisionError dega.

# try :- try block mein wo code likhte hain jisme exception aa sakta hai.
# except :- except block exception aane par execute hota hai.

# Example :-
try:
    a = 10
    b = 0
    print(a / b)

except:
    print("Error Occurred")

# Specific Exception :- Hum particular type ke exception ko bhi handle kar sakte hain.

try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

# ValueError :- Jab wrong type/value ki input di jati hai tab ValueError aa sakta hai.

try:
    number = int(input("Enter Number :- "))
    print(number)

except ValueError:
    print("Please Enter Number Only")

# TypeError :- Jab incompatible data types ke saath operation kiya jata hai.

try:
    a = 10
    b = "20"
    print(a + b)

except TypeError:
    print("Different Data Types Cannot Be Added")

# IndexError :- Jab list ke available index se bahar ka index access karte hain.
try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Index Does Not Exist")

# KeyError :- Jab dictionary mein jo key exist nahi karti usko access karte hain.
try:
    student = {
        "name": "Shubham",
        "age": 23
    }
    print(student["marks"])

except KeyError:
    print("Key Does Not Exist")
    
# Multiple except :- Ek try block ke saath multiple except blocks use kar sakte hain.
try:
    a = int(input("Enter Number :- "))
    b = int(input("Enter Number :- "))
    print(a / b)
    
except ValueError:
    print("Enter Numbers Only")

except ZeroDivisionError:
    print("Cannot Divide By Zero")

# else :- else block tab execute hota hai jab try block successfully execute ho jaye. Agar exception aata hai to else execute nahi hota.
try:
    a = 10
    b = 2
    print(a / b)

except ZeroDivisionError:
    print("Cannot Divide By Zero")
else:
    print("Division Successfully Completed")

# finally :- finally block hamesha execute hota hai. Exception aaye ya na aaye, finally execute hota hai.
try:
    a = 10
    b = 2
    print(a / b)

except ZeroDivisionError:
    print("Cannot Divide By Zero")

finally:
    print("Program Finished")

# try + except + else + finally :-
try:
    a = int(input("Enter First Number :- "))
    b = int(input("Enter Second Number :- "))
    result = a / b

except ValueError:
    print("Enter Numbers Only")

except ZeroDivisionError:
    print("Cannot Divide By Zero")
else:
    print("Result :-", result)
finally:
    print("Program Finished")

# Types of Exceptions :-Python mein commonly used exceptions :-
# 1. ZeroDivisionError
# 2. ValueError
# 3. TypeError
# 4. IndexError
# 5. KeyError
# 6. NameError
# 7. FileNotFoundError
# 8. AttributeError

# NameError :- Jab koi variable define kiye bina use kiya jata hai.
try:
    print(name)
    
except NameError:
    print("Variable Is Not Defined")
    
# FileNotFoundError :- Jab file exist nahi karti aur usko open karne ki koshish karte hain.
try:
    file = open("abc.txt", "r")

except FileNotFoundError:
    print("File Not Found")

# Exception Handling ka Basic Structure :-
try:
    # Risky Code
    pass

except:
    # Exception Code
    pass

else:
    # Successful Code
    pass

finally:
    # Always Execute
    pass

# Important Points :-
# 1. try block mein risky code likha jata hai.
# 2. except exception ko handle karta hai.
# 3. Multiple except use kar sakte hain.
# 4. else tab execute hota hai jab exception nahi aata.
# 5. finally hamesha execute hota hai.
# 6. Different exceptions ke liye different except blocks use kar sakte hain.
# 7. Exception Handling program ko unexpectedly stop hone se bachane mein help karti hai.