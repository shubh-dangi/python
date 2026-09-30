# Number Collection Analyzer — Array + Function
# Ek program banao jo user se 10 integers accept kare aur array mein store kare.
# Program mein:
# array module import karo.
# Integer array create karo.
# 10 numbers input lekar array mein add karo.
# Array ko display karo.
# Array ka total aur average calculate karo.
# Ek number search karo aur uski position display karo.
# Kisi given number ki occurrence count karo.
# Array ko ascending order mein Bubble Sort se sort karo.
# Ek function analyze_array() banao jo analysis kare.

# Use karna hai :- from array import array , append() , index() , count() , len() , Loop , Function , return , Bubble Sort
from array import array


def analyze_array(numbers):
    print("\nArray:", numbers)
    total = 0
    for num in numbers:
        total += num
    print("Total:", total)

    average = total / len(numbers)
    print("Average:", average)

    search = int(input("Enter number to search: "))
    if search in numbers:
        print("Number Found")
        print("Position:", numbers.index(search))
        print("Count:", numbers.count(search))
    else:
        print("Number Not Found")

    for i in range(len(numbers)):
        for j in range(0, len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print("Sorted Array:", numbers)

    return total, average


numbers = array('i')
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

total, average = analyze_array(numbers)
print("\nTotal:", total)
print("Average:", average)
print("Array as List:", numbers.tolist())