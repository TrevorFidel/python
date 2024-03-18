class Person:
    def __init__(self, Name,Age,Gender,Year_of_Birth,):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Year_of_Birth = Year_of_Birth
psn1 = Person('Trevor', 21,'Male', 2003)
psn2 = Person('Neema', 22,'Female', 2004)
psn3 = Person('Buraha', 24,'Female', 2005)
print(f'{psn1.Name} of age {psn1.Age} is a {psn1.Gender} and was born in {psn1.Year_of_Birth}')
print(f'{psn2.Name} of age {psn2.Age} is a {psn2.Gender} and was born in {psn2.Year_of_Birth}')
class Students(Person):
    def __init__(self, Name, Age, Gender, Year_of_Birth, Admin,):
        super().__init__(Name,Age, Gender, Year_of_Birth)
        self.Admin = Admin
std1 = Students("Trevor", 21,'Male',2003,12413)
std2 = Students("Neema", 22,"Female",2004, 12576)
print(f'{std1.Name} of age {std1.Age} is a {std1.Gender} born in {std1.Year_of_Birth} of admission number {std1.Admin}')
print(f'{std2.Name} of age {std2.Age} is a {std2.Gender} born in {std2.Year_of_Birth} of admission number {std2.Admin}')
class Employees(Person):
    def __init__(self, Name, Age, Gender, Year_of_Birth, Salary):
        super().__init__(Name,Age, Gender,Year_of_Birth)
        self.Salary = Salary
emp1 = Employees("Joel",21,'Male',2003, 300000)
emp2 = Employees("Bob",22,'Female',2004, 400000)
print(f'{emp1.Name} of age {emp1.Age} is a {emp1.Gender} born in {emp1.Year_of_Birth} earns {emp1.Salary}')
print(f'{emp2.Name} of age {emp2.Age} is a {emp2.Gender} born in {emp2.Year_of_Birth} earns {emp2.Salary}')
