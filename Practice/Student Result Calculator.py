# User se 3 subjects ke marks input lo aur
# Total marks calculate karo
# Percentage calculate karo
# Percentage ke basis par Grade print karo
# Use: input(), type conversion, arithmetic operators, if-elif-else, f-string

sub1=int(input("Enter Subject 1 Mark :- "));
sub2=int(input("Enter Subject 2 Mark :- "));
sub3=int(input("Enter Subject 3 Mark :- "));

total=sub1+sub2+sub3;
print("Subject 1 Mark :- ",sub1,"\nSubject 2 Mark :- ",sub2,"\nSubject 3 Mark :- ",sub3)
print(f"Total Marks :- {total}")

percentage=(total*100)/300
print(f"Percentage :- {percentage}")

grade="";
if percentage>=91 and percentage <=100:
    grade="A";
elif percentage>=81 and percentage<=90:
    grade="B";
elif percentage>=71 and percentage<=80:
    grade="C";
elif percentage>=61 and percentage<=70:
    grade="D";
elif percentage>=51 and percentage<=60:
    grade="E";
else:
    grade="Fail";
print(f"Your Grade is :- {grade}")