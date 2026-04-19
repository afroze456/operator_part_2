weight= float(input("enter your weight in meters:"))
height= float(input("enter your height in kg:"))

BMI = weight/height**2
if BMI<18.5:
    print("you are underweight")
elif BMI<25:
    print("you are healthy")
elif BMI<30:
    print("you are over weight")
elif BMI<35:
    print("you are severly over weiht")
elif BMI<40:
    print("you are obese")
else:
    print("you are severly obese")