
# arithmetic_operators
# +,-,*,/,%,**
a = 5
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
# assignment_operators
c = 10
# c = c + 5
c+=5
print(c)
d = 7
d =d - 4
# d-=4
print(d)
c = 8
c = c * 2
# c*=2
a = 4
a = a/2
# a/=2
print(a)
# comparison_operators
# ==,!=, <=, >=, <, >
a = 10
b = 20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
# logical_operators
# and, or, not
t = 6
f = 8
print((t>f) and (t<f))
print((t<f) and (t>f))
print((t>f) and (t==f))
print((t<f) and (t==f))
print((t>f) and (t<=f))
print((t>f) or (t<f))
print((t<f) or (t>f))
print((t>f) or (t==f))
print((t<f) or (t==f))
print((t>f) or (t<=f))
print(not((t>f) or (t<f)))
print(not((d>f) or (d<f)))
# identity_operator // is, is not
x = 6
y = 3
print(x is y)
print(x is not y)
print(type(x) is type(y))
# membership operator
a = "Welcome to Fullstack Devolopment"
print('Welcome' in a)
print('stack' in a)
print('Full' not in a)
z = input("Number of chickens in your farm ")
y = input("Number of ducks in your ")
print(z<y)
age = 15
if age >= 18:
    print("You are old enough to move out")
    print("You are expected to have an ID")
else: print("You are young to move out")

grade = 70
if grade >= 80 and grade <= 100:
    print("You are an A material")
elif grade >= 70 and grade <= 80:
    print("You are a B material")
elif grade >= 70 and grade >=50:
    print("You are a C material")
elif grade <= 50 and grade >=40:
    print("You are a D material")
elif grade <= 40 and grade >=20:
    print("You are a E material")
elif grade <= 20 and grade >=0:
    print("You are a F material")
else:
    print("Kindly key in appropriate marks")

