# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# The BMI is defined as the body mass divided by the square of the body
# height, and is expressed in units of kg/m2.

print(round((float(weight))/(float(height)**2)))

# The teacher tends to define a lot of extra variables. This might be to
# to improve readability, particularly for beginners, but variables use
# up memory. IMO this code is perfectly readable. 