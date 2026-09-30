# Common & Unique Numbers — Set + Array + Function
# Do collections banao.
# User se :- First collection ke 5 integers , Second collection ke 5 integers

# input lo.
# Dono ko array mein store karo.
# Uske baad:
# Dono arrays ko set mein convert karo.
# Common elements find karo.
# First collection ke unique elements find karo.
# Second collection ke unique elements find karo.
# Dono collections ke saare unique elements find karo.
# Check karo ki dono sets disjoint hain ya nahi.
# Ek function compare_numbers() banao jo ye complete comparison kare.
# Results display karo.

# Use karna hai :- Array , Set , set() , & / intersection() , - / difference() , | / union() , isdisjoint() , Function , return , Loop

from array import array

def compare_numbers(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    print("\nFirst Set:", set1)
    print("Second Set:", set2)

    common = set1 & set2
    print("Common Numbers:", common)

    unique_first = set1 - set2
    print("Only First Array:", unique_first)

    unique_second = set2 - set1
    print("Only Second Array:", unique_second)

    all_numbers = set1 | set2
    print("All Numbers:", all_numbers)

    if set1.isdisjoint(set2):
        print("Both Sets are Disjoint")
    else:
        print("Both Sets are Not Disjoint")

    return common, all_numbers

arr1 = array('i')
arr2 = array('i')
print("Enter 5 numbers for First Array")

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    arr1.append(num)

print("\nEnter 5 numbers for Second Array")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    arr2.append(num)

common, all_numbers = compare_numbers(arr1, arr2)