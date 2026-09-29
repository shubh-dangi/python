# Loops :- Loop ka use kisi code ko baar-baar execute karne ke liye hota hai.
# Python me mainly 2 loops hain :- for loop , while loop
# Aur inke saat :- range() , nested loops , break , continue , pass , for-else , while-else

# 1. for Loop :- Jab hume pata ho ki kisi sequence ke elements par iterate karna hai, tab for use karte hain.
# Syntax :- 
# for variable in sequence:
    # code
for i in range(5):
    print(i)

# 2. range() :- range() numbers ki sequence generate karta hai.
# range(stop) :- when only stop value given 
for i in range(5):
    print(i)

# range(start, stop) :- start and end value ho 
for i in range(2, 6):
    print(i)

# range(start, stop, step) :- tino valve ho tab
for i in range(1, 10, 2):
    print(i)

# if You Want Reverse order :- 
for i in range(5, 0, -1):
    print(i)

# 3. for Loop with String :- String ke characters par bhi loop laga sakte hain.
name = "Python"
for ch in name:
    print(ch)

# 4. for Loop with List :- 
numbers = [10, 20, 30, 40]
for x in numbers:
    print(x)
# Yaani for loop iterable objects jaise string, list, tuple, set, dictionary etc. par kaam kar sakta hai.

# 5. while Loop :- while loop tab tak execute hota hai jab tak condition True hai.
# Syntax :-
# while condition:
    # code
    
i = 1
while i <= 5:
    print(i)
    i += 1
# while me condition ko eventually False banana zaroori hai

# 6. Nested Loop :- Ek loop ke andar doosra loop = nested loop.
for i in range(3):
    for j in range(2):
        print(i, j)
# Nested loops ka use mostly patterns, matrices, tables etc. me hota hai.

# 7. break :- break loop ko immediately stop karta hai.
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# 9. continue :- continue current iteration ko skip karta hai aur next iteration par chala jata hai.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
# 10. pass :- pass ka matlab hai kuch mat karo.
for i in range(5):
    pass

# 11. for-else :-Python me for ke saath else bhi use kar sakte hain.

for i in range(5):
    print(i)
else:
    print("Loop completed")
# Note :- else tab execute hota hai jab loop normally complete ho.

# 12. while-else :-while ke saath bhi else use kar sakte hain.
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Completed")

# 13. Loop with if :- Loops aur conditions commonly saath use hote hain.
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# 14. Infinite Loop :- Aisa loop jo kabhi end nahi hota.
while True:
    print("Hello")