print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice1 = input('You\'re at the crossroads, where do you want to go? Type "left" or "right".  ').lower()

if choice1 == "left" :

    if choice1 == "right":
        print("Fell into into a hole. Game Over.")
else:
    print("Game Over.")

choice2 = input(' you\'re currently in the swimming pool, what you wanna do ? Type "Swim" or "wait". ').lower()
if choice2 == "wait":
    if choice2 == "swim":
        print("there is a trout spotted , you were attacked by the trout . Game over.")
else :
    print("Game over")

choice3 = input('your in front of a door , you have three options choose one "red" or "yellow" or "blue" ').lower()
print("you entered a fire realm, you got burnt by fire")
if choice3 == "yellow":
    print("You win the eternal treasure")
if choice3 == "blue":
    print("You entered into a beast realm , you got eaten by the beasts, Game Over.")
else:
    print("Game over")
