weight = int(input("enter your weight : "))
height = float(input("enter your height : "))

BMI = weight / (height **2)

if BMI < 18.5:
    print("underweight")
elif 18.5 <= BMI < 24.9:
    print("normal weight")
elif 25 <= BMI < 29.9:
    print("over weight")
else :
    print("obesity")


