height = float(input("Enter you height (M): "))
weight = float(input("Enter you weight(Kg): "))
bmi = weight/ height * 2
print("Your bmi is ", bmi)
if  bmi>=1 and bmi < 18:
    print("Under-Weight")
elif bmi >= 18 and bmi <=24:
    print("Normal")
elif bmi >=25 and bmi <=30:
    print("Overweight")
elif bmi >30:
    print("Abnormal")
else:
    print("invalid")