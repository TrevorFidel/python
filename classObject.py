class Student:  
    name = 'Fidel'
    age = 21
print(Student.name)
print(Student.age)
print(f'Name: {Student.name} Age: {Student.age}')
class Employees:
    name = 'Joel'
    salary = 50
    residence = 'Syokimau'
print(f'Employees name is: {Employees.name}  '
      f'and earns a Salary of: {Employees.salary}: '
      f'and Resides in : {Employees.residence}')
class Parents:
    first_name = 'Danstun'
    last_name = 'Nyongesa'
parent1 = Parents()
print(parent1.first_name)

class Parent:
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
parent1 = Parent('Danstun','Nyongesa')
print(parent1.first_name)
parent2 = Parent('Magret','Wambudo')
print(f'parents first name: {parent2.first_name} second name: {parent2.last_name}')
print(f'parents first name: {parent1.first_name} second name: {parent1.last_name}')

class Presidents:
    def __init__(self, first_name, last_name, years_of_ruling):
        self.first_name = first_name
        self.last_name = last_name
        self.years_of_ruling = years_of_ruling
president1 = Presidents('Jomo', 'Kenyatta',15)
president2 = Presidents('Daniel', 'Moi', 21)
president3 = Presidents('Mwai','kibaki', 10)
print(f'First Name: {president1.first_name}  Last Name: {president1.last_name}   Years Ruled: {president1.years_of_ruling}')
print(f'First Name: {president2.first_name}  Last Name: {president2.last_name}   Years Ruled: {president2.years_of_ruling}')
print(f'First Name: {president3.first_name}  Last Name: {president3.last_name}   Years Ruled: {president3.years_of_ruling}')

class Person:
    def __init__(self,first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        print(f'{self.first_name} {self.last_name} is {self.age} years old')
    def display(self):
        print(f'{self.age}')
person1 = Person('Jomo', 'Kenyatta', 56)
print(person1.full_name())
print(person1.display())
person2 = Person('Daniel', 'Moi',76)
print(person2.full_name())
print(person2.display())