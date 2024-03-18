class Staff:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
staff1 = Staff("John","Mwaura",40)
staff2 = Staff("shosh","Waganjo",75)
print(f'  {staff1.firstName} {staff1.lastName} of age {staff1.age} is a teacher.')
print(f'  {staff2.lastName} {staff2.firstName} of age {staff2.age} is the catress')
class Teacher(Staff):
    def __init__(self,firstName,lastName,age,salary):
        super().__init__(firstName, lastName, age)
        self.salary = salary
T1 = Teacher("John","Mwaura",40,60000)
T2 = Teacher("Joel","Macibo",60,100000)
print(f'{T1.firstName} {T1.lastName} is {T1.age} of age and earns an income of about {T1.salary} ' )
print(f'{T2.firstName} {T2.lastName} is {T2.age} of age and earns an income of about {T2.salary}')
