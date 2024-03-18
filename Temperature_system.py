temp = float(input("Enter you body temperature in Celsius:"))
if temp < 20:
    print("Put on a sweater")
elif temp >= 20 and temp <30:
    print("Put on a shirt")
elif temp >= 30 and temp <40:
    print("Remove the shirt")