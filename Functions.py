
def Hello_world():
    print("Hello World")
    print("Hello World")
    print("Hello World")
def nyumba(name):
    print("name")
    print("name")
    print("name")
nyumba("Trevor")
nyumba("Cecilia")
nyumba("Joel")
def num(nambari):
    print(nambari)
    print(nambari)
    print(nambari)
num(56)
def num1(fname):
    print(fname + " is my favorite person")
num1("Alex")
num1("Esther")
def students(first_name, last_name):
    print(first_name + last_name + " Please enter your number")
students('Trevor', ' Fidel')
def employees(first_name, age):
    if age <20:
        print(first_name + "You are below 20 years")
    elif age <=30:
        print(first_name + "You are middle aged")
    else:
        print(first_name + "You are older than 30 years")
employees('Trevor ', 21)
employees("Fidel",24)

def age_calculator(age):
    new_age = age + 10
    return new_age
calculated_age = age_calculator(21)
print(calculated_age)

def age_calculator(age):
    new_age = age - 7
    return new_age
calculated_age = age_calculator(21)
print(calculated_age)
def performance_calculator(*subjects):
    total = sum(subjects)
    return total
perf = performance_calculator(45,56)
print(perf)
student2 = performance_calculator(23,67)
print(student2)
student3 = performance_calculator(23,56,67)
print(student3)
def description_calculator(first_name,height,weight ):
    total = height + weight
    return first_name, total
team = description_calculator("Trevor",89,60)
print(team)
def country(nchi = "Ivory Coast"):
    return nchi
print(country("Jamaica"))
print(country("Kenya"))
print(country("Britain"))
print(country())

def ongeza(x):
    return x * x
ongeza = ongeza(5)
print(ongeza)