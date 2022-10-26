# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m2.

BMI = round((float(weight))/(float(height)**2))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI <= 25:
    print(f"Your BMI is {BMI}, you have a normal weight")
elif BMI <= 30:
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, you are obese")
else:
    print(f"Your BMI is {BMI}, you are clinically obese")