# Inheritance :- Ek class ki properties aur methods ko dusri class mein use karne ko Inheritance kehte hain.
# Parent Class :- Jis class se properties aur methods inherit hote hain.
# Child Class :- Jo class Parent Class ki properties aur methods ko inherit karti hai.

# 1. Basic Inheritance
class Student:
    def display(self):
        print("Student Information")

class BCA(Student):
    pass

student1 = BCA()
student1.display()
# BCA class ne Student class ka display() method inherit kiya.


# 2. Parent Class aur Child Class
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog1 = Dog()
dog1.eat()
dog1.bark()
# Dog child class hai.
# Animal parent class hai.


# 3. Single Inheritance :- Ek Child Class ek Parent Class se inherit karti hai.
class Person:
    def show_person(self):
        print("Person Information")

class Student(Person):
    def show_student(self):
        print("Student Information")

student1 = Student()
student1.show_person()
student1.show_student()
# Student ne Person se inheritance kiya.


# 4. Constructor in Inheritance
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name :-", self.name)

class Student(Person):
    def display_student(self):
        print("Student Information")

student1 = Student("Shubham")
student1.display_person()
student1.display_student()
# Child class parent class ke constructor ko use kar sakti hai.


# 5. super()
# super() :- Parent class ke method ya constructor ko child class ke andar call karne ke liye use hota hai.
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display(self):
        print("Name :-", self.name)
        print("Course :-", self.course)

student1 = Student("Shubham", "BCA")
student1.display()
# super().__init__(name)
# Parent class ke __init__() ko call karta hai.

# 6. Multilevel Inheritance :- Jab ek class dusri class se inherit kare aur teesri class us child class se inherit kare.
class GrandParent:
    def display_grandparent(self):
        print("Grand Parent")

class Parent(GrandParent):
    def display_parent(self):
        print("Parent")

class Child(Parent):
    def display_child(self):
        print("Child")

child1 = Child()
child1.display_grandparent()
child1.display_parent()
child1.display_child()
# GrandParent → Parent → Child

# 7. Hierarchical Inheritance :- Jab multiple child classes ek hi Parent class se inherit karti hain.
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

dog1 = Dog()
cat1 = Cat()
dog1.eat()
dog1.bark()
cat1.eat()
cat1.meow()
# Dog aur Cat dono Animal se inherit kar rahe hain.

# 8. Multiple Inheritance :- Jab ek Child Class multiple Parent Classes se inherit karti hai.
class Father:
    def father_property(self):
        print("Father Property")

class Mother:
    def mother_property(self):
        print("Mother Property")

class Child(Father, Mother):
    def child_property(self):
        print("Child Property")

child1 = Child()
child1.father_property()
child1.mother_property()
child1.child_property()
# Child ne Father aur Mother dono se inheritance kiya.

# 9. Method Overriding :- Jab Child Class Parent Class ke same method ko apne according dobara define karti hai.
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barking")

animal1 = Animal()
dog1 = Dog()
animal1.sound()
dog1.sound()
# Dog class ne Parent ke sound() method ko override kar diya.


# Polymorphism :- Same method/function ka different objects ke liye different behaviour hona Polymorphism kehlata hai.
# 10. Polymorphism using Method Overriding
class Dog:
    def sound(self):
        print("Dog Barking")

class Cat:
    def sound(self):
        print("Cat Meowing")

dog1 = Dog()
cat1 = Cat()
dog1.sound()
cat1.sound()
# Same method name sound() Lekin different objects ke liye different output.

# 11. Polymorphism with Function
class Dog:
    def sound(self):
        print("Dog Barking")

class Cat:
    def sound(self):
        print("Cat Meowing")

def make_sound(animal):
    animal.sound()

dog1 = Dog()
cat1 = Cat()
make_sound(dog1)
make_sound(cat1)
# make_sound() same function hai. Lekin different objects ke according different method call hota hai.

# 12. Polymorphism with Different Classes
class Student:
    def display(self):
        print("Student Information")

class Teacher:
    def display(self):
        print("Teacher Information")

student1 = Student()
teacher1 = Teacher()
student1.display()
teacher1.display()
# Dono classes mein display() method hai. Lekin dono ka behaviour different hai.

# Encapsulation :- Data aur methods ko ek class ke andar combine karna Encapsulation kehlata hai.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :-", self.name)
        print("Age :-", self.age)

student1 = Student("Shubham", 23)
student1.display()
# Data aur methods ek hi class ke andar hain.

#  Public Variable :- Normal variable ko class ke bahar bhi directly access kiya ja sakta hai.
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Shubham")
print(student1.name)
# name public variable hai.


# Protected Variable :- Variable ke naam ke starting mein single underscore (_) lagaya jata hai.
class Student:
    def __init__(self, name):
        self._name = name

student1 = Student("Shubham")
print(student1._name)
# _name protected variable hai.

# Private Variable :- Variable ke naam ke starting mein double underscore (__) lagaya jata hai.
class Student:
    def __init__(self, name):
        self.__name = name

student1 = Student("Shubham")
# print(student1.__name) Directly access nahi karna chahiye.

# 16. Private Variable ko Method se Access Karna
class Student:
    def __init__(self, name):
        self.__name = name

    def display(self):
        print("Name :-", self.__name)

student1 = Student("Shubham")
student1.display()
# Private variable ko class ke method ke through access kar sakte hain.

# 17. Getter :- Private data ko read/access karne ke liye method banaya jata hai.
class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

student1 = Student("Shubham")
print(student1.get_name())
# get_name() private variable ki value return karta hai.

# 18. Setter :- Private data ki value ko update/change karne ke liye method banaya jata hai.
class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

student1 = Student("Shubham")
print(student1.get_name())
student1.set_name("Rahul")
print(student1.get_name())
# set_name() private variable ki value update karta hai.


# Abstraction :- Abstraction ka matlab hai unnecessary details ko hide karna aur sirf important information ko user ke saamne show karna. Python mein abstraction ke liye abc module ka use kar sakte hain.
# abc :- Abstract Base Class
# ABC :- Abstract Base Class banane ke liye use hota hai.
# abstractmethod :- Abstract method banane ke liye use hota hai.

# Example :-
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog makes sound")

d = Dog()
d.sound()

# Important :- Abstract class ka direct object nahi bana sakte.
# Example :-
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
# a = Animal()  # Ye error dega because Animal abstract class hai.

# Abstract Method :- Abstract method wo method hota hai jiska declaration abstract class mein hota hai lekin implementation child class mein hoti hai.

# Example :-
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

c = Car()
c.start()
b = Bike()
b.start()

# Abstraction with Constructor :-
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print(self.name, "is doing coding")

d = Developer("Shubham")
d.work()

# Multiple Abstract Methods :-
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")

    def display(self):
        print("Rectangle Shape")

r = Rectangle()
r.area()
r.display()

# Abstraction + Inheritance :-
# Abstract class parent class hoti hai.
# Child class abstract methods ko implement karti hai.

# Important Points :-
# 1. Abstraction unnecessary details ko hide karti hai.
# 2. Python mein abc module abstraction ke liye use hota hai.
# 3. ABC se abstract class banayi ja sakti hai.
# 4. @abstractmethod se abstract method banaya jata hai.
# 5. Abstract class ka direct object nahi bana sakte.
# 6. Child class ko abstract method implement karna compulsory hota hai.
# 7. Abstract class mein normal methods bhi ho sakte hain.

# Simple Difference :-
# Encapsulation :- Data ko protect/hide karna.
# Abstraction :- Implementation/details ko hide karke sirf important functionality show karna.