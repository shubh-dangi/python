# 1. Arithmetic Operators :- +(Addition) , -(Subtraction) , *(Multiplication) , /(Division) , %(Remainder) , //(Floor Division) , **(Power)
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333
print(a % b)   # 1
print(a // b)  # 3
print(a ** b)  # 1000

# 2. Comparison Operators :- ==(Equal) , !=(Not equal) , >(Greater) , <(Smaller) , >=(Greater/equal) , <=(Smaller/equal)
a = 10
b = 5

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False

# 3. Assignment Operators :- 
a = 10

a += 5   # 15
a -= 2   # 13
a *= 2   # 26
a /= 2   # 13.0
a %= 5   # 3.0
a //= 2  # 1.0
a **= 2  # 1.0

# 4. Logical Operators :- and(Both conditions true) , or(At least one true) , not(Reverse result)
a = 10

print(a > 5 and a < 20)  # True
print(a > 20 or a < 15)  # True
print(not(a > 5))        # False

# 5. Membership Operators :- in(Present hai) , not in(Present nahi hai)
name = "shubham"

print("s" in name)       # True
print("x" not in name)   # True

# 6. Identity Operators :- is(Same object) , is not(Different object)
a = 10
b = 10

print(a is b)       # True
print(a is not b)   # False
# Note :-  == aur 'is' same nahi hain.

# 7. Bitwise Operators :- &(AND) , ^(XOR) , ~(NOT) , <<(Left Shift) , >>(Right Shift)
a = 5
b = 3

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2