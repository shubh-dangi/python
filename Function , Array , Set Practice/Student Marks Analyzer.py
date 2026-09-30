# Student Marks Analyzer — Set + Function
# Ek program banao jo students ke marks ko analyze kare.
# User se 10 marks input lo.

# Program ko:
# Marks ko ek list mein store karna hai.
# List ko set mein convert karke duplicate marks remove karne hain.
# Total unique marks display karo.
# Highest aur lowest unique marks find karo.
# User se ek mark input lekar check karo ki wo marks mein present hai ya nahi.
# Ek function analyze_marks() banao jo ye analysis kare.
# Function se result return karo.
# Use karna hai :- list , set() , in ,Function , return , Loop , max() , min()

def analyze_marks(marks_list):
    marks_set=set(marks_list)
    print("All Marks :- ",marks_list)
    print("Unique Marks :- ",marks_set)
    
    print("\n Highest Value in set :- ",max(marks_set))
    print("\n Lowest Value in Set :- ",min(marks_set))
    
    search=int(input("Enter Number To Search :- "))
    if search in marks_set:
        print("Number Got Found")
    else:
        print("Number Not Found")

    print("Function Finished")
    return marks_set


marks_list=[]
for i in range(10):
    marks=int(input(f"Enter Numbers {i+1}:- "))
    marks_list.append(marks)

j=1
for i in marks_list:
    print(f"Number {j} :- {i}")
    j+=1

result=analyze_marks(marks_list)
print(result)