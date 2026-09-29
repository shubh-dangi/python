#every string has a unicod charecter
#if you want to check unicode use ord

a="A";
print(ord(a))

#if you want to covert unicode to charecter use 'chr'
b=65
print(chr(b))

#string me har charecter ko indexing di jati hai 0 - se start hoti aur n number tak 

student="shubham"
print(student[0])
print(student[1])
print(student[2])
print(student[3])
print(student[4])
print("\n\n")   #\n use for next line ,\t use for tab 
# agr ap indexing ko negative me le jaoge to ulta chalega 
print(student[-0])
print(student[-1])
print(student[-2])
print(student[-3])
print(student[-4])

# string slicing :- get some part from string 
# str[starting index : ending index : steps]
name='shubham dangi'
print(name[0:6:1])