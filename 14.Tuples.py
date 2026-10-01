# Tuple :- Python mein Tuple ek ordered collection hota hai jisme hum multiple values store kar sakte hain.
# Tuple:
# 1. Ordered hota hai
# 2. Immutable hota hai
# 3. Duplicate values allow karta hai
# 4. Different data types ke elements store kar sakta hai
# Tuple ko () round brackets se create kiya jata hai.

# 1. Creating a Tuple :-
numbers = (10, 20, 30, 40, 50)
print(numbers)

# Different data types ke elements
data = (10, "Shubham", 20.5, True)
print(data)

# Empty Tuple
empty_tuple = ()
print(empty_tuple)

# 2. Creating Tuple without () :- Python mein brackets ke bina bhi Tuple create kar sakte hain. Isko tuple packing kehte hain.
numbers = 10, 20, 30, 40
print(numbers)
print(type(numbers))

# 3. Single Element Tuple :- Single element Tuple banane ke liye comma lagana zaroori hai.
number = (10,)
print(number)
print(type(number))

# Agar comma nahi lagaya:
number = (10)
print(type(number)) # Ye Tuple nahi hai. Ye int hai.

#  4. Accessing Tuple Elements :- Tuple ke elements ko index number se access karte hain. Index 0 se start hota hai.
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# 5. Negative Indexing :- Negative indexing mein last element ka index -1 hota hai.
numbers = (10, 20, 30, 40, 50)
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])

# 6. Tuple Slicing :- Tuple ke kuch elements ko nikalne ke liye slicing use karte hain.
# Syntax :- tuple[start : stop]
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

# Starting se
print(numbers[:3])

# Kisi index se end tak
print(numbers[2:])

# Step ke saath
print(numbers[::2])

# 7. Tuple is Immutable :- Tuple immutable hota hai. Isliye Tuple ke existing element ko change nahi kar sakte.
numbers = (10, 20, 30)
# numbers[0] = 100
# Ye Error dega.


# List mutable hoti hai :-
numbers_list = [10, 20, 30]
numbers_list[0] = 100
print(numbers_list)

# 8. Tuple Concatenation :- Do Tuples ko + operator se join kar sakte hain.
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
result = tuple1 + tuple2
print(result)

# 9. Tuple Repetition :- * operator ki help se Tuple ko repeat kar sakte hain.
numbers = (1, 2, 3)
result = numbers * 3
print(result)

# 10. Membership Operators :-
# in :- Check karta hai ki element Tuple mein present hai ya nahi.
numbers = (10, 20, 30, 40, 50)
print(30 in numbers)
print(100 in numbers)

# not in :- Check karta hai ki element Tuple mein present nahi hai.
print(100 not in numbers)
print(30 not in numbers)

# 11. Traversing a Tuple :- for loop ki help se Tuple ke har element ko access kar sakte hain.
numbers = (10, 20, 30, 40, 50)
for num in numbers:
    print(num)

# Index ke saath Tuple traverse karna
for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])

# 12. len() :- len() Tuple ke total elements ki number batata hai.
numbers = (10, 20, 30, 40, 50)
print(len(numbers))

# 13. max() :- max() Tuple ki sabse badi value return karta hai.
numbers = (10, 50, 20, 80, 30)
print(max(numbers))

# 14. min() :- min() Tuple ki sabse chhoti value return karta hai.
numbers = (10, 50, 20, 80, 30)
print(min(numbers))

# 15. sum() :- sum() Tuple ke numeric elements ka total return karta hai.
numbers = (10, 20, 30, 40, 50)
print(sum(numbers))

# 16. count() :- count() batata hai ki koi value Tuple mein kitni baar present hai.
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# 17. index() :- index() kisi element ka index return karta hai.
numbers = (10, 20, 30, 40)
print(numbers.index(30))

# 18. Average of Tuple :-Tuple ka average nikalne ke liye :- Average = Total / Number of Elements
numbers = (10, 20, 30, 40, 50)
total = sum(numbers)
average = total / len(numbers)
print("Total:", total)
print("Average:", average)

# 19. Traversing and Calculating Tuple :-
numbers = (10, 20, 30, 40, 50)
total = 0
for num in numbers:
    total += num
print("Total:", total)

# 20. Nested Tuple :- Tuple ke andar Tuple ko Nested Tuple kehte hain.
numbers = ((10, 20, 30),(40, 50, 60),(70, 80, 90))
print(numbers)

# 21. Accessing Nested Tuple :-
numbers = ((10, 20, 30),(40, 50, 60),(70, 80, 90))
print(numbers[0])
print(numbers[0][0])
print(numbers[1][2])
print(numbers[2][1])


# 22. Traversing Nested Tuple :-
numbers = ((10, 20, 30),(40, 50, 60),(70, 80, 90))
for row in numbers:
    for value in row:
        print(value)

# 23. Sorting a Tuple :- Tuple immutable hota hai. Isliye tuple.sort() method available nahi hota.
# sorted() function use karke Tuple ko sort kar sakte hain.
# sorted() result ko List ke form mein return karta hai.
numbers = (50, 20, 40, 10, 30)
result = sorted(numbers)
print(result)

# 24. Sorting Tuple in Descending Order :-
numbers = (50, 20, 40, 10, 30)
result = sorted(numbers, reverse=True)
print(result)

# 25. Sorting Nested Tuple :- Nested Tuple ko bhi sorted() se sort kar sakte hain.
numbers = ((30, 20),(10, 50),(20, 40))
result = sorted(numbers)
print(result)

# 26. Tuple Packing :- Multiple values ko ek Tuple mein store karna Tuple Packing kehlata hai.
student = "Shubham", 23, "BCA"
print(student)

# 27. Tuple Unpacking :- Tuple ke elements ko multiple variables mein assign karna Tuple Unpacking kehlata hai.
student = ("Shubham", 23, "BCA")
name, age, course = student
print(name)
print(age)
print(course)

# 28. Converting List into Tuple :-
numbers_list = [10, 20, 30, 40, 50]
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)

# 29. Converting Tuple into List :-
numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)
print(numbers_list)

# 30. Searching an Element :-
numbers = (10, 20, 30, 40, 50)
search = int(input("Enter number to search: "))
if search in numbers:
    print("Number Found")
else:
    print("Number Not Found")

# 31. Maximum and Minimum :-
numbers = (10, 50, 20, 80, 30)
maximum = max(numbers)
minimum = min(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)

# 32. Tuple Methods :- Tuple mein mainly ye methods hote hain:
# count() -> value kitni baar present hai
# index() -> value ka index return karta hai
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))
print(numbers.index(20))

# 33. Important Tuple Functions :-
# len()   -> total elements
# max()   -> maximum value
# min()   -> minimum value
# sum()   -> total of numeric values
# sorted() -> sorted List return karta hai
numbers = (10, 20, 30, 40, 50)
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

# Tuple vs List
# List:
# 1. Ordered hoti hai
# 2. Mutable hoti hai
# 3. [] brackets use karti hai
# 4. More methods available hote hain

# Tuple:
# 1. Ordered hota hai
# 2. Immutable hota hai
# 3. () brackets use karta hai
# 4. count() aur index() methods available hain
# Tuple mein element update nahi kar sakte.