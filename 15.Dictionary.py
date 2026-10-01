# Dictionary :- Python mein Dictionary ek collection hota hai jisme data Key : Value pair mein store hota hai.
# Dictionary:
# 1. Key : Value pair mein data store karti hai
# 2. Keys unique hoti hain
# 3. Mutable hoti hai
# 4. Different data types ki values store kar sakti hai
# 5. Dictionary {} curly brackets se create hoti hai.

# 1. Creating a Dictionary :-
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
print(student)

# 2. Empty Dictionary :- 
student = {}
print(student)

# 3. Key and Value :-
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}

# 4. Accessing Dictionary Values :-
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
print(student["name"])
print(student["age"])
print(student["course"])

# 5. Accessing using get() :- get() ki help se value access kar sakte hain.
student = {
    "name": "Shubham",
    "age": 23
}
print(student.get("name"))
print(student.get("age"))

# Agar key exist nahi karti:
print(student.get("mobile"))
# get() normally None return karta hai.

# 6. Adding New Element :-
student = {
    "name": "Shubham",
    "age": 23
}
student["course"] = "BCA"
print(student)

# 7. Updating Existing Value :-
student = {
    "name": "Shubham",
    "age": 23
}
student["age"] = 24
print(student)

# 8. update() :- update() ki help se ek ya multiple values update/add kar sakte hain.
student = {
    "name": "Shubham",
    "age": 23
}
student.update({
    "age": 24,
    "course": "BCA"
})
print(student)

# 9. Removing Element using pop() :- pop() specified key ko remove karta hai.
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
student.pop("age")
print(student)

# 10. popitem() :- popitem() last inserted key-value pair remove karta hai.
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
student.popitem()
print(student)

# 11. clear() :- clear() Dictionary ke saare elements remove karta hai.
student = {
    "name": "Shubham",
    "age": 23
}
student.clear()
print(student)

# 12. del :- del ki help se particular key remove kar sakte hain.
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
del student["age"]
print(student)
# Puri Dictionary delete karna:
# del student

# 13. Dictionary Membership :- in operator Dictionary ki keys ko check karta hai.
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
print("name" in student)
print("mobile" in student)

# not in
print("mobile" not in student)

# 14. keys() :- keys() Dictionary ki saari keys return karta hai.
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
print(student.keys())

# 15. values() :- values() Dictionary ki saari values return karta hai.
print(student.values())

# 16. items() :- items() key-value pairs return karta hai.
print(student.items())

# 17. Traversing Dictionary using keys :- 
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
for key in student:
    print(key)


# 18. Traversing Dictionary using values :-
for value in student.values():
    print(value)

# 19. Traversing Dictionary using items() :-
for key, value in student.items():
    print(key, ":", value)

# 20. len() :- len() Dictionary ke total key-value pairs batata hai.
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
print(len(student))

# 21. Dictionary with Different Data Types :-
data = {
    "name": "Shubham",
    "age": 23,
    "marks": 85.5,
    "passed": True
}
print(data)

# 22. Dictionary with List as Value :-
student = {
    "name": "Shubham",
    "subjects": ["Python", "JavaScript", "PHP"]
}
print(student)
print(student["subjects"])
print(student["subjects"][0])

# 23. Nested Dictionary :- Dictionary ke andar Dictionary ko Nested Dictionary kehte hain.
students = {
    "student1": {
        "name": "Shubham",
        "age": 23
    },
    "student2": {
        "name": "Rahul",
        "age": 22
    }
}
print(students)

# 24. Accessing Nested Dictionary :-
print(students["student1"])
print(students["student1"]["name"])
print(students["student2"]["age"])

# 25. Traversing Nested Dictionary :-
for student_id, details in students.items():
    print("Student ID:", student_id)
    for key, value in details.items():
        print(key, ":", value)

# 26. Dictionary from Two Lists :- Do Lists ko Dictionary mein convert karne ke liye zip() aur dict() use kar sakte hain.
keys = ["name", "age", "course"]
values = ["Shubham", 23, "BCA"]
student = dict(zip(keys, values))
print(student)

# 27. List into Dictionary :- List of pairs ko Dictionary mein convert kar sakte hain.
data = [
    ("name", "Shubham"),
    ("age", 23),
    ("course", "BCA")
]
student = dict(data)
print(student)

# 28. Dictionary from List using range() :-
numbers = list(range(1, 6))
squares = {}
for num in numbers:
    squares[num] = num * num
print(squares)

# 29. Searching a Key :-
student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
search = input("Enter key to search: ")
if search in student:
    print("Key Found")
    print("Value:", student[search])
else:
    print("Key Not Found")

# 30. Updating Dictionary using User Input :-
student = {
    "name": "Shubham",
    "age": 23
}
key = input("Enter key: ")
value = input("Enter value: ")
student[key] = value
print(student)

# 31. Dictionary with Cricket Players :-
players = {
    "Virat": 80,
    "Rohit": 75,
    "Rahul": 65,
    "Hardik": 50
}
print(players)

# Display players and scores
for player, score in players.items():
    print(player, ":", score)

# 32. Finding Highest Score :-
players = {
    "Virat": 80,
    "Rohit": 75,
    "Rahul": 65,
    "Hardik": 50
}
highest = max(players.values())
print("Highest Score:", highest)

# 33. Dictionary in Function :-
def display_student(student):
    for key, value in student.items():
        print(key, ":", value)

student = {
    "name": "Shubham",
    "age": 23,
    "course": "BCA"
}
display_student(student)

# 34. Function Returning Dictionary :-
def create_student():
    student = {
        "name": "Shubham",
        "age": 23,
        "course": "BCA"
    }
    return student
result = create_student()
print(result)

# 35. Copying Dictionary :-
student1 = {
    "name": "Shubham",
    "age": 23
}
student2 = student1.copy()
student2["age"] = 24
print(student1)
print(student2)

# Important Dictionary Methods :-
# get()      -> value access karna
# keys()     -> saari keys
# values()   -> saari values
# items()    -> key-value pairs
# update()   -> add/update elements
# pop()      -> specified key remove
# popitem()  -> last key-value pair remove
# clear()    -> saare elements remove
# copy()     -> Dictionary ki copy