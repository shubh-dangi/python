# Type Conversion = ek data type ko doosre data type mein convert karna.
a = "10"
b = int(a)

print(b)
print(type(b))

# 1. int() — Integer mein convert
a = "25"
b = int(a)
print(b)

# 2. float() — Float mein convert
a = "25.5"
b = float(a)
print(b)

# 3. str() — String mein convert
a = 25
b = str(a)
print(b)
print(type(b))

# 4. boolean() — Boolean mein convert
a = 10
b = bool(a)
print(b)

"""
Basic rule:
bool(0)      # False
bool(10)     # True
bool("")     # False
bool("hello")# True"""

# 5. complex() — Complex number mein convert
a = 10
b = complex(a)
print(b)    #(10+0j)

# 6. list() — List mein convert
a = "hello"
b = list(a)
print(b)    #['h', 'e', 'l', 'l', 'o']

# 7. tuple() — Tuple mein convert
a = [1, 2, 3]
b = tuple(a)
print(b)    #(1, 2, 3)

# 8. set() — Set mein convert
a = [1, 2, 2, 3]
b = set(a)
print(b)    #{1, 2, 3} Duplicate values remove ho gayi.

# 9. dict() — Dictionary mein convert , Isme data key-value pairs ke form mein hona chahiye.
a = [("name", "shubham"), ("age", 23)]
b = dict(a)
print(b)    #{'name': 'shubham', 'age': 23}

# Note :- Type Conversion generally hum explicitly function laga kar karte hain , Isko explicit conversion bhi bolte hain.
# Python kabhi-kabhi khud bhi conversion karta hai; usse implicit type conversion kehte hain:
a = 10
b = 2.5
c = a + b
print(c)