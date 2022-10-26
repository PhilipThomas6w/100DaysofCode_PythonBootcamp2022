#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the bill calculator.")
bill = float(input("How much is the total bill?\n"))
size_of_party = int(input("How many people are you splitting the bill between?\n"))
tip_percentage = float(input("What percentage of the bill do you want to leave as a tip?\n"))

# Below, the second argument, 2, is the number of decimal places we want to round our result too. However, if it ends in a 0, then that 0 will be cut off.
bill_per_person = round((bill / size_of_party) * (1 + (tip_percentage / 100)), 2)

# This next line will return a float with two decimal places, even if the last digit is 0.
bill_per_person = "{:.2f}".format(bill_per_person)

print(f"The final bill for each person is ${bill_per_person}")    