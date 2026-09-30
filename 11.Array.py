# Array :- Python mein array ek collection hota hai jisme same type ke elements store kiye ja sakte hain.
# Simple words :- Array mein multiple values ko ek variable mein store kar sakte hain.
# Python mein array use karne ke liye array module import karna padta hai.
from array import array
# Array create kaise karein?
numbers = array('i', [10, 20, 30, 40])
print(numbers)
# 'i' ka matlab :- integer type array. Is array mein integer values store hongi.

# Array ke advantages:
# 1. Multiple values ko ek variable mein store kar sakte hain.
# 2. Same type ke elements store kar sakte hain.
# 3. Indexing aur slicing kar sakte hain.
# 4. Array ke elements ko modify kar sakte hain.

# Array ke elements ko access karna
numbers = array('i', [10, 20, 30, 40])
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
# Index hamesha 0 se start hota hai.

# Array mein element update karna
numbers = array('i', [10, 20, 30, 40])
numbers[1] = 50
print(numbers)

# Slicing :- Array ke ek range ke elements ko access karna.
numbers = array('i', [10, 20, 30, 40, 50])
print(numbers[1:4])

# Array processing :- Loop ka use karke array ke elements ko process kar sakte hain.
numbers = array('i', [10, 20, 30, 40])
for number in numbers:
    print(number)

# Array mein element add karna
# append() :- Array ke end mein ek element add karta hai.
numbers = array('i', [10, 20, 30])
numbers.append(40)
print(numbers)

# insert() :- Kisi particular position par element add karta hai.
numbers = array('i', [10, 20, 30])
numbers.insert(1, 50)
print(numbers)

# remove() :- Given element ko array se remove karta hai.
numbers = array('i', [10, 20, 30, 40])
numbers.remove(20)
print(numbers)

# pop() :- Array se element remove karta hai , aur removed element ko return karta hai.
numbers = array('i', [10, 20, 30, 40])
x = numbers.pop()
print(x)
print(numbers)

# index() :- Kisi element ki position find karta hai.
numbers = array('i', [10, 20, 30, 40])
print(numbers.index(30))

# count() :- Kisi element ki occurrence count karta hai.
numbers = array('i', [10, 20, 20, 30, 20])
print(numbers.count(20))

# tolist() :- Array ko list mein convert karta hai.
numbers = array('i', [10, 20, 30, 40])
new_list = numbers.tolist()
print(new_list)

# Array mein search karna
numbers = array('i', [10, 20, 30, 40, 50])
value = 30
if value in numbers:
    print("Element found")
else:
    print("Element not found")

# Array mein element ki position search karna
numbers = array('i', [10, 20, 30, 40, 50])
value = 40
print("Position:", numbers.index(value))

# Bubble Sort :- Bubble sort mein adjacent elements ko compare karke bade element ko gradually end ki taraf bheja jata hai.
numbers = array('i', [40, 10, 30, 20, 50])
n = len(numbers)
for i in range(n):
for j in range(0, n - i - 1):
    if numbers[j] > numbers[j + 1]:
        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(numbers)

# Bubble sort ke baad array ascending order mein aa jayega.
# Indexing aur Slicing ek saath
numbers = array('i', [10, 20, 30, 40, 50, 60])
print(numbers[0])       # First element
print(numbers[2])       # Third element
print(numbers[1:5])     # Range of elements
print(numbers[:3])      # Starting ke 3 elements
print(numbers[3:])      # 3rd index se end tak

# Array mein negative indexing bhi use kar sakte hain.
numbers = array('i', [10, 20, 30, 40, 50])
print(numbers[-1])      # Last element
print(numbers[-2])      # Second last element

# Array ko update karna
numbers = array('i', [10, 20, 30, 40])
numbers[0] = 100
print(numbers)

# Array ke elements ko loop se display karna
numbers = array('i', [10, 20, 30, 40])
for i in range(len(numbers)):
    print(numbers[i])