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
print("Make your choice.")

choice = input("left or "
               "right? \n:").lower()
#even if you hit enter in the middle of the sentence and change line it wont change, good for visibility
# choise = input('You\'re in a dark room with two path ahead. "left" or "right"? :')

if choice == "left" or choice == "Left":
    print("You can swim or wait for the other pirates to arrive to bring a small boat.")
    choice = input("swim or wait? \n:")
    if choice == "wait" or choice == "Wait":
        choice = input("Pick a door. Red,Blue,Yellow \n:")
        if choice == "yellow" or choice == "Yellow":
            print("You win!")
        elif choice == "red" or choice == "Red":
            print("Burned by fire. Game over.")
        elif choice == "blue" or choice == "Blue":
            print("Eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")