# Student Result Management System :- Ek program banao jo 5 students ka complete result system manage kare.
# Requirements:
# Har student ke liye :- Student ID , Student Name , Course , 5 Subjects ke marks
# Data ko appropriate List, Tuple aur Dictionary mein store karo.

# Program ko ye kaam karne chahiye:
# 5 students ka data input lo.
# Student ke subjects ke marks ko List mein store karo.
# Student ki basic information (id, name, course) ko Tuple mein store karo.
# Har student ka complete data Dictionary mein store karo.

# students = {
#     101: {
#         "info": (101, "Rahul", "BCA"),
#         "marks": [78, 85, 67, 90, 72]
#     }
# }

# Sabhi students ka data display karo.
# Har student ke :- Total marks , Average , Highest mark , Lowest mark , calculate karo.
# Jis student ka average 40 ya usse zyada ho usko Pass, otherwise Fail.
# Student ID se student search karo. Student name se student search karo.
# Kisi particular subject ke marks sabhi students ke liye display karo.
# Sabhi students mein :- Highest total , Lowest total , find karo.
# Sabhi student names ko ek separate List mein nikalo.
# Sabhi courses ko ek Tuple mein convert karo.
# Student ID aur total marks ko ek separate Dictionary mein store karo.
# Marks ke basis par students ko highest-to-lowest order mein display karo.
# Kisi student ke marks mein ek new mark add karo using List operation.
# Kisi student ke marks se ek mark remove karo.
# Dictionary ke keys(), values() aur items() ka use karke data traverse karo.
# Concepts you MUST use :- List , Tuple , Dictionary , Indexing , Negative indexing , Slicing , append() , insert() , remove() , pop() , count() , index() , sort() , reverse() , in , not in , len() , max() , min() , sum() , keys() , values() , items() , get() , update() , nested list , nested dictionary , list → tuple , tuple → list , dictionary search
students = {}

for i in range(5):
    student_id = int(input("Enter Student ID :- "))
    name = input("Enter Student Name :- ")
    course = input("Enter Course :- ")
    marks = []
    for j in range(5):
        mark = int(input(f"Enter Subject {j+1} Marks :- "))
        marks.append(mark)

    student_data = (student_id, name, course)
    student = {
        "student_data": student_data,
        "student_marks": marks
    }
    students[student_id] = student
print(students)

print("\n========== STUDENT RESULT ==========")
for student_id, student in students.items():
    student_data = student["student_data"]
    marks = student["student_marks"]
    name = student_data[1]
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    if average >= 40:
        result = "Pass"
    else:
        result = "Fail"
    print("\nStudent ID :-", student_id)
    print("Student Name :-", name)
    print("Marks :-", marks)
    print("Total Marks :-", total)
    print("Average :-", average)
    print("Highest Mark :-", highest)
    print("Lowest Mark :-", lowest)
    print("Result :-", result)