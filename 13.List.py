# List :- Python mein List ek ordered collection hota hai , jisme hum multiple values store kar sakte hain.

# List:
# 1. Ordered hoti hai
# 2. Mutable hoti hai
# 3. Duplicate values allow karti hai
# 4. Different data types ke elements store kar sakti hai
# List ko [] square brackets se create kiya jata hai.


# 1. Creating a List :-
numbers = [10, 20, 30, 40, 50]
print(numbers)


# Different data types ki values bhi store kar sakte hain.
data = [10, "Shubham", 20.5, True]
print(data)


# Empty List :-
empty_list = []
print(empty_list)


# 2. Accessing List Elements
# List ke elements ko index number se access karte hain. Index hamesha 0 se start hota hai.
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# 3. Negative Indexing :- Negative indexing mein last element ka index -1 hota hai.
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])


# 4. List using range() :- range() ki help se list create kar sakte hain.
numbers = list(range(1, 11))
print(numbers)

# Step ke saath
numbers = list(range(1, 11, 2))
print(numbers)

# 5. Updating List Elements :- List mutable hoti hai. Isliye hum existing element ko change kar sakte hain.
numbers = [10, 20, 30, 40, 50]
numbers[2] = 100
print(numbers)

# Multiple elements update
numbers[0] = 500
numbers[4] = 900
print(numbers)

# 6. List Concatenation :- Do lists ko + operator se join kar sakte hain.
list1 = [10, 20, 30]
list2 = [40, 50, 60]
result = list1 + list2
print(result)

# 7. List Repetition :- * operator ki help se list ko repeat kar sakte hain.
numbers = [1, 2, 3]
result = numbers * 3
print(result)

# 8. Membership Operators
# in :- Check karta hai ki element List mein present hai ya nahi.
numbers = [10, 20, 30, 40, 50]
print(30 in numbers)
print(100 in numbers)


# not in :- Check karta hai ki element List mein present nahi hai.
print(100 not in numbers)
print(30 not in numbers)

# 9. Traversing a List :- for loop ki help se List ke har element ko access kar sakte hain.
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)

# Index ke saath
for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])

#10. len() Function :- len() List ke total elements ki number batata hai.
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

# 11. Aliasing :- Jab ek List ko directly dusre variable mein assign karte hain, dono variables same List ko refer karte hain. Isko Aliasing kehte hain.
list1 = [10, 20, 30]
list2 = list1
list2[0] = 100
print(list1)
print(list2)
# Yahan list1 aur list2 same List ko refer kar rahe hain.

# 12. Cloning :- Cloning mein original List ki ek alag copy create hoti hai.
list1 = [10, 20, 30]
list2 = list1.copy()
list2[0] = 100
print(list1)
print(list2)
# Dono Lists alag hain.

#13. append() :- append() List ke end mein ek element add karta hai.
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# 14. insert() :- insert(index, value) , Kisi specific position par element add karta hai.
numbers = [10, 20, 30]
numbers.insert(1, 100)
print(numbers)

# 15. remove() :- remove() List mein se specified value ko remove karta hai.
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)

# 16. pop() :- pop() List se element remove karta hai. Agar index nahi diya to last element remove hota hai.
numbers = [10, 20, 30, 40]
numbers.pop()
print(numbers)

# Specific index ka element remove
numbers.pop(1)
print(numbers)

# 17. index() :-index() kisi element ki position/index return karta hai.
numbers = [10, 20, 30, 40]
print(numbers.index(30))

# 18. count() :- count() batata hai ki koi value List mein kitni baar present hai.
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))

# 19. sort() :- sort() List ko ascending order mein arrange karta hai.
numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)

# Descending order
numbers.sort(reverse=True)
print(numbers)

#  20. reverse() :- reverse() List ke elements ka order reverse karta hai.
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

# 21. Nested List :- List ke andar List ko Nested List kehte hain.
numbers = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
print(numbers)

# Nested List ke elements access karna
print(numbers[0])
print(numbers[0][0])
print(numbers[1][2])
print(numbers[2][1])

# 22. Nested List using Loop :-
numbers = [[10, 20, 30],[40, 50, 60],[70, 80, 90]]
for row in numbers:
    for value in row:
        print(value)

# 23. List Slicing :- List ka kuch part nikalne ke liye slicing use karte hain.
# Syntax :- list[start : stop]
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

# Starting se
print(numbers[:3])

# End tak
print(numbers[2:])

# Step
print(numbers[::2])

# 24. List with User Input :- 
numbers = []
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
print("List:", numbers)

# 25. Searching an Element :- 
numbers = [10, 20, 30, 40, 50]
search = int(input("Enter number to search: "))
if search in numbers:
    print("Number Found")
else:
    print("Number Not Found")

#  26. Finding Maximum and Minimum :- 
numbers = [10, 50, 20, 80, 30]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# 27. Sum of List :-
numbers = [10, 20, 30, 40, 50]
print("Sum:", sum(numbers))