print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

decision1 = input('You\'ve arrived at a crossroad. Which way do you go? Type "left" or "right".\n').lower()

# Using the lower() function, above, means the answer could be "left" or "LEFT" or "Left", for example. It saves us from having to type "left" or "LEFT" or "Left"...

if decision1 == "left":
    decision2 = input(
        'After several hours of walking, you come upon an inland sea. There is an island in the centre of it. Type "wait" to wait for a boat, or type "swim" to swim to the island.\n').lower()

    if decision2 == "wait":
        decision3 = input(
            'You arrive at the island and come across a strange building with three doors: one red, one yellow, and one blue. Which door do you enter? Type "red", "blue", or "yellow"?\n').lower()

        if decision3 == "red":
            print("You are burned by fire. Game over!")
        elif decision3 == "blue":
            print("You are eaten by vicious beasts. Game over!")
        elif decision3 == "yellow":
            print("You found the treasure. You win!)")
        else:
            print("You waited too long. The building vanishes before your eyes. Game over!")

    else:
        print("You are attacked by an angry trout. Game over!")

else:
    print("You fall into a hole. Game over!")

