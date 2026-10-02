# Class :- Python mein class ek blueprint/template hoti hai jiske through hum objects create karte hain.
# Object :- Class ka instance/object hota hai. Object ke andar data aur methods hote hain.

# 1. Class Create Karna
class Student:
    pass
# pass :- Jab class ke andar abhi koi code nahi likhna ho
# tab pass use kar sakte hain.

# 2. Object Create Karna
class Student:
    pass
student1 = Student()
student2 = Student()
print(student1)
print(student2)

# 3. Attribute :- Object ke andar stored data ko attribute kehte hain.
class Student:
    pass

student1 = Student()
student1.name = "Shubham"
student1.age = 23
student1.course = "BCA"
print(student1.name)
print(student1.age)
print(student1.course)

# 4. Multiple Objects
class Student:
    pass

student1 = Student()
student2 = Student()
student1.name = "Shubham"
student1.age = 23
student2.name = "Rahul"
student2.age = 22
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
# Har object ka apna data ho sakta hai.

# 5. Method :- Class ke andar banaya gaya function method kehlata hai.
class Student:
    def display(self):
        print("Student Information")

student1 = Student()
student1.display()
# display() ek method hai.

# 6. self Keyword :- Current object ko represent karta hai. self ki help se hum current object ke attributes aur methods ko access karte hain.
class Student:
    def display(self):
        print("Student Name")

student1 = Student()
student1.display()
# Jab student1.display() call hota hai, tab self student1 object ko represent karta hai.


# 7. __init__() Method :- Ye special method hai.
# Object create hote hi automatically call hota hai.Iska use object ke attributes ko initialize karne ke liye hota hai.
class Student:
    def __init__(self):
        print("Student Object Created")

student1 = Student()

# 8. __init__() with Parameters
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Shubham", 23)
print(student1.name)
print(student1.age)
# self.name :- Object ka attribute
# name :- Parameter

# 9. Instance Variables :- Aise variables jo har object ke liye alag-alag values store karte hain.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Shubham", 23)
student2 = Student("Rahul", 22)
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
# student1 aur student2 ke attributes alag hain.

# 10. Instance Method :- Aisa method jo object ke data ke saath kaam karta hai aur self use karta hai.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name :-", self.name)
        print("Age :-", self.age)

student1 = Student("Shubham", 23)
student1.display()

# 11. Multiple Methods
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name :-", self.name)
        print("Age :-", self.age)
        print("Course :-", self.course)

    def message(self):
        print("Student Information Displayed")

student1 = Student("Shubham", 23, "BCA")
student1.display()
student1.message()

# 12. Class Variable :- Aisa variable jo class ke sabhi objects ke liye common hota hai.
class Student:
    college = "ABC College"
    def __init__(self, name):
        self.name = name

student1 = Student("Shubham")
student2 = Student("Rahul")
print(student1.name)
print(student1.college)
print(student2.name)
print(student2.college)
# college class variable hai. name instance variable hai.

# 13. Instance Variable vs Class Variable
class Student:
    college = "ABC College"
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Shubham", 23)
student2 = Student("Rahul", 22)
print(student1.name)
print(student2.name)
print(student1.college)
print(student2.college)
# name aur age :- Instance Variables
# college :- Class Variable

# 14. Class Variable Update
class Student:
    college = "ABC College"
    def __init__(self, name):
        self.name = name

student1 = Student("Shubham")
print(student1.college)
Student.college = "XYZ College"
print(student1.college)
# ClassName.variable se class variable access/update kar sakte hain.

# 15. Object ke Attributes Access Karna
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Shubham", 23)
print(student1.name)
print(student1.age)

# 16. Attribute Update Karna
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Shubham", 23)
print(student1.name)
student1.name = "Rahul"
print(student1.name)
# Object ke attribute ko update kar sakte hain.

# 17. Method ke andar Calculation
class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total(self):
        result = self.marks1 + self.marks2 + self.marks3
        print("Total Marks :-", result)

student1 = Student(80, 75, 90)
student1.total()

# 18. Method Returning Value
class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total(self):
        result = self.marks1 + self.marks2 + self.marks3
        return result

student1 = Student(80, 75, 90)
result = student1.total()
print("Total Marks :-", result)

# 19. Student Complete Example
class Student:
    college = "ABC College"
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name :-", self.name)
        print("Age :-", self.age)
        print("Course :-", self.course)
        print("College :-", self.college)

student1 = Student("Shubham", 23, "BCA")
student1.display()

# 20. Multiple Student Objects
class Student:
    college = "ABC College"
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name :-", self.name)
        print("Age :-", self.age)
        print("Course :-", self.course)
        print("College :-", self.college)

student1 = Student("Shubham", 23, "BCA")
student2 = Student("Rahul", 22, "BCA")
student3 = Student("Amit", 24, "BCA")
student1.display()
print()
student2.display()
print()
student3.display()