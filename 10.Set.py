# Set :- Python mein set ek unordered collection of unique elements hota hai.
# Simple words :- Set mein duplicate values nahi hoti.
numbers = {10, 20, 30, 40}
print(numbers)

# Duplicate values automatically remove ho jaati hain.
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)
# Note :- Set indexing support nahi karta.
# Duplicates allowed nahi.
# Set ko modify kar sakte ho.
# Normally tum set mein ye rakh sakte ho :- int, float, str, tuple, bool
# Lekin mutable objects jaise :- list, dict, set
# set ke elements nahi ban sakte.

# Set create kaise karein?
s = {10, 20, 30}
print(s)
s = set()       # Ye empty set banata hai.
print(s)
s = {}          # Ye empty set nahi hai. Ye empty dictionary hai.
print(type(s))

# List ko Set mein convert karna
numbers = [10, 20, 20, 30, 30]
s = set(numbers)
print(s)        # Duplicates remove ho jayenge.

# Set mein indexing nahi hoti.
numbers = {10, 20, 30}
# print(numbers[0])     # Error
# Kyunki set unordered collection hai.

# Set ko traverse karne ke liye:
for value in numbers:
    print(value)

# add() :- Set mein ek element add karta hai.
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# update() :- Multiple elements add karne ke liye use hota hai.
numbers = {10, 20}
numbers.update([30, 40, 50])
print(numbers)

# remove() :- Set se element remove karta hai.
numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)

# discard() :- Set se element remove karta hai.
# Element nahi mila to error nahi deta.
numbers = {10, 20, 30}
numbers.discard(20)
print(numbers)
# remove() aur discard() ka difference:
# remove() -> element nahi mila to error
# discard() -> element nahi mila to error nahi

# pop() :- Set se koi element remove karke return karta hai.
numbers = {10, 20, 30}
x = numbers.pop()
print(x)
print(numbers)
# Set unordered hai,
# isliye kaunsa element remove hoga ye assume nahi karna.

# clear() :- Set ke saare elements remove karta hai.
numbers = {10, 20, 30}
numbers.clear()
print(numbers)

# len() :- Set mein kitne elements hain ye batata hai.
numbers = {10, 20, 30, 40}
print(len(numbers))

# in operator :- Check karta hai element set mein hai ya nahi.
numbers = {10, 20, 30}
print(20 in numbers)

# not in :- Check karta hai element set mein nahi hai.
numbers = {10, 20, 30}
print(50 not in numbers)

# Union :- Dono sets ke saare unique elements.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
print(A.union(B))

# Intersection :- Jo elements dono sets mein common hain.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)
print(A.intersection(B))

# Difference :- First set mein hain,
# second set mein nahi.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A - B)
print(A.difference(B))

# Symmetric Difference :-
# Dono sets mein jo elements hain,
# lekin common nahi hain.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A ^ B)
print(A.symmetric_difference(B))

# issubset() :-
# Check karta hai ki first set ke saare elements
# second set mein hain ya nahi.
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))

# issuperset() :-
# Check karta hai ki first set mein
# second set ke saare elements hain ya nahi.
A = {1, 2, 3, 4}
B = {1, 2}
print(A.issuperset(B))

# isdisjoint() :-
# Check karta hai ki dono sets mein
# ek bhi common element nahi hai.
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))

# Agar common element hai to False milega.
A = {1, 2}
B = {2, 3}
print(A.isdisjoint(B))

# copy() :- Set ki copy banata hai.
A = {10, 20, 30}
B = A.copy()
print(A)
print(B)

# Set comparison :-
# == check karta hai ki dono sets ke elements same hain ya nahi.
A = {1, 2, 3}
B = {3, 2, 1}
print(A == B)
# Order matter nahi karta.

# != :- Check karta hai ki dono sets different hain ya nahi.
A = {1, 2}
B = {1, 2, 3}
print(A != B)
# Set mein duplicate automatically remove ho jaate hain.
names = {"Ram", "Shyam", "Ram", "Mohan"}
print(names)

# Isi wajah se list ke duplicates remove kar sakte hain.
numbers = [1, 2, 2, 3, 3, 4]
numbers = set(numbers)
print(numbers)

# Set mein different datatypes rakh sakte hain.
s = {10, 20.5, "Hello", True}
print(s)

# Set ke andar list nahi rakh sakte.
# s = {[1, 2], [3, 4]}     # Error
# Set ke andar tuple rakh sakte hain.
s = {(1, 2), (3, 4)}
print(s)

# frozenset :- Frozenset bhi set ki tarah
# unique elements ka collection hota hai.
# Lekin frozenset ko modify nahi kar sakte.
numbers = frozenset([10, 20, 30, 40])
print(numbers)

# Frozenset mein duplicate values nahi hoti.
numbers = frozenset([10, 20, 20, 30, 30])
print(numbers)

# Frozenset ko modify nahi kar sakte.
numbers = frozenset([10, 20, 30])
# numbers.add(40)       # Error
# numbers.remove(20)    # Error
# Frozenset mein common set operations use kar sakte hain.

A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

# Frozenset mein membership check kar sakte hain.
A = frozenset([10, 20, 30])
print(20 in A)

# Frozenset mein len() use kar sakte hain.
print(len(A))

# Frozenset mein subset check kar sakte hain.
A = frozenset([1, 2])
B = frozenset([1, 2, 3, 4])
print(A.issubset(B))

# Frozenset mein superset check kar sakte hain.
print(B.issuperset(A))

# Frozenset mein disjoint check kar sakte hain.
C = frozenset([5, 6])
print(A.isdisjoint(C))