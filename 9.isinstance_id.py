# 1. isinstance() ka use hum check karne ke liye karte hain ki koi object kisi particular datatype/class ka hai ya nahi.
# Syntax :-
# isinstance(object, type)
x = 10
print(isinstance(x, int))


# 2. id() & Object References :- Python mein har object ka ek identity hota hai. id() us object ki identity ka integer representation deta hai.
x = 10
print(id(x))

# Do variables same object ko refer kar sakte hain
a = 10
b = a
print(id(a))
print(id(b))
# Dono names same object ko refer kar sakte hain.
a is b  #True ho sakta hai.

a = [10, 20]
b = [10, 20]
print(a == b)

# 3. Mutable vs Immutable
# Mutable object ko create karne ke baad uske contents ko modify/change kar sakte ho.
numbers = [10, 20, 30]
numbers[0] = 100
print(numbers)  #[100, 20, 30]
# Common mutable types :- list , dict , set -> Inke contents modify kiye ja sakte hain.

# Immutable object ko create hone ke baad directly modify nahi kar sakte.
# Common examples :- int , float , bool , str , tuple
name = "Shubham"
name[0] = "R"   #Ye error dega.