class Employees:
    def __init__(self,name, gender, salary):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.email = name + "@gmail.com"
    def full_name(self):
        return self.name
    def salary_increase(self):
        self.salary = int(self.salary *1.05)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
class Developer(Employees): ##WHEN MAKING ACHILD CLASS PUT THE PARENT CLASS// //##//INHERITANCE,..
    def __init__(self, name, gender, salary, program_language):
        super().__init__(name, gender, salary)
        self.program_language =program_language
developer1 = Developer("Grace","Female",60000,"Python")
developer2 = Developer("Simon","Male",50000,"Javascript")
print(f'  {developer1.full_name()} earning {developer1.salary} and develops with {developer1.program_language}')
print(f'  {developer2.full_name()} earning {developer2.salary} and develops with {developer2.program_language}')
class Receptionist(Employees):
    def __init__(self , name, gender, salary, age):
        super().__init__(name, gender, salary)
        self.age = age
Rec1 = Receptionist("Joy",'Female',20000,"45")
Rec2 = Receptionist("Mercy", "Female",30000,"25")
print(f'  {Rec1.full_name()} is a {Rec1.gender} earning an income of {Rec1.salary} and is {Rec1.age} years old')

emp1 = Employees("Trevor", " Male", 100000)
emp2 = Employees("Cecilia", " Female", 200000)
print(emp1.name)
print(emp2.name)
print(emp1.email)
print(emp2.email)
print(f'{emp1.name} is a {emp1.gender} and earns {emp1.salary}')
print(f'{emp2.name} is a {emp2.gender} and earns {emp2.salary}')
print(emp1.full_name())
print(emp1.salary)
emp1.salary_increase()
print(emp1.salary)
print(emp2.salary)
emp2.salary_increase()
print(emp2.salary)

Employees.set_raise_amount(1.07)
print(Employees.raise_amount)
print(emp1.salary)
print(emp2.salary)
#### ASSESMENT


class Students:
    def __init__(self, first_name, second_name, maths, english):
        self.first_name = first_name
        self.second_name = second_name
        self.maths = maths
        self.english = english
    def total_marks(self):
        return self.maths + self.english
std1 = Students("Joel", "Smith", 70,56)
std2 = Students("Terquila","Neema",75, 50)
print(std1.total_marks())
print(std2.total_marks())
print(f'{std1.first_name} {std1.second_name} scored {std1.total_marks()} marks.')
print(f'{std2.first_name} {std2.second_name} scored {std2.total_marks()} marks.')


## attempt

class Person:
    def __init__(self, name, residence, age,):
        self.name = name
        self.residence = residence
        self.age = age
class Occupation(Person):
    def __init__(self, name, residence, age, occupation):
        super().__init__(name, residence, age)
        self.occupation = occupation
class Salary(Occupation):
    def __init__(self, name, residence, age, occupation, salary):
        super().__init__(name, residence,age, occupation)
        self.salary = salary
sal1 = Salary("Joel", "Kisumu", 40, "teacher", 40000)
sal2 = Salary("Mabonga","Kitale", 30, "doctor",50000)
print(f'{sal1.name} resides in {sal1.residence} of age {sal1.age} working  earning {sal1.salary}')
