# 1. None :- None Python ka ek special value hai jo represent karta hai , “Abhi koi value nahi hai” / “No value”
name = None
print(name)
# Yahan name variable exist karta hai, lekin uske andar koi actual data/value nahi hai.

# 2. NoneType :- None ki datatype NoneType hoti hai.
x = None
print(type(x))

# 3. None vs 0 :- Ye dono same nahi hain.
a = None
b = 0
print(a == b)
# 0 ek actual integer value hai.

# 4. None vs empty string "" :-Ye bhi different hain.
a = None
b = ""
print(a == b)
# Matlab name ki value currently assigned nahi hai.

# 5. None ko check kaise karte hain?
# Python mein recommended way hai:
name = None
if name is None:
    print("Name is not available")

# 6. Function mein None
# Ye None ka bahut important use hai. Agar function koi value explicitly return nahi karta, to Python generally None return karta hai.
def hello():
    print("Hello")
result = hello()
print(result)