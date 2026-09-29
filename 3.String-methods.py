# 1. upper() — Capital letters mein convert karna
name = "shubham"
print(name.upper())

# 2. lower() — Small letters mein convert karna
name = "SHUBHAM"
print(name.lower())

# 3. capitalize() — First letter capital krna
name = "shubham"
print(name.capitalize())

# 4. title() — Har word ka first letter capital
name = "shubham kumar"
print(name.title())

# 5. strip() — Extra spaces remove karna , String ke starting aur ending ke spaces remove karta hai.
name = "   shubham   "
print(name.strip())

# 6. replace() — Text replace karna
# Syntax: string.replace(old, new)
name = "I like Java"
print(name.replace("Java", "Python"))

# 7. split() — String ko parts/list mein todna, String ko todkar list bana deta hai.
name = "shubham kumar"
print(name.split())

# Note :- By default, space ke according split karta hai.

# 8. join() — List/String parts ko jodna , split() ka roughly opposite samajh sakte ho.
names = ["shubham", "ramu", "karan"]
result = "-".join(names)
print(result)

# 9. find() — Text ki position find karna , String ke andar kisi character/word ki index position find karta hai.
name = "shubham"
print(name.find("h"))

# 10. count() — Kitni baar aaya
name = "shubham"
print(name.count("h"))

text = "python is easy and python is powerful"
print(text.count("python"))

# 11. startswith() — Starting check karna , Check karta hai ki string given text se start hoti hai ya nahi. Result hamesha True ya False hota hai.
name = "shubham"
print(name.startswith("shu"))

# 12. endswith() — Ending check karna , Check karta hai ki string given text par end hoti hai ya nahi.
name = "shubham"
print(name.endswith("ham"))

# 13. isdigit() — Sirf digits check karna , Check karta hai ki string mein sirf numbers/digits hain ya nahi.
number = "12345"
print(number.isdigit())

# 14. isalpha() — Sirf alphabets check karna , Check karta hai ki string mein sirf letters hain ya nahi.
name = "shubham"
print(name.isalpha())

# 15. isalnum() — Alphabet + Number , Check karta hai ki string mein sirf alphabets aur numbers hain.
data = "shubham123"
print(data.isalnum())