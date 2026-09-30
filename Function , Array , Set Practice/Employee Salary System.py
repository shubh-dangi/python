# Employee Salary System — Functions
# Ek employee salary program banao.
# User se :- Employee name , Basic salary , HRA , DA , PF
# input lo.
# Functions banao :- calculate_hra() , calculate_da() , calculate_pf() , calculate_gross() ,calculate_net()
# Rules :- Gross Salary = Basic + HRA + DA , Net Salary = Gross - PF

# Program mein:
# Har calculation ke liye separate function use karo.
# Functions se values return karo.
# calculate_gross() ko required values arguments ke through do.
# calculate_net() ko gross aur PF pass karo.
# Final employee salary report display karo.

# Use karna hai :- Functions , Parameters , Arguments , return , Multiple functions , Positional arguments

def calculate_hra(basic):
    hra = basic * 0.20
    return hra

def calculate_da(basic):
    da = basic * 0.10
    return da

def calculate_pf(basic):
    pf = basic * 0.12
    return pf

def calculate_gross(basic, hra, da):
    gross = basic + hra + da
    return gross

def calculate_net(gross, pf):
    net = gross - pf
    return net

name = input("Enter Employee Name: ")
basic = float(input("Enter Basic Salary: "))

hra = calculate_hra(basic)
da = calculate_da(basic)
pf = calculate_pf(basic)
gross = calculate_gross(basic, hra, da)
net = calculate_net(gross, pf)

print("\n----- Employee Salary Details -----")
print("Employee Name:", name)
print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross)
print("PF:", pf)
print("Net Salary:", net)