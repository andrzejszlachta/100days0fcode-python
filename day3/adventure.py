print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
Welcome to Treasure Island.
Your mission is to find the treasure.''')

crossroad_choice = input('''You're at a cross road. Where do you want to go?
            Type "left" or "right"
''').lower()
if crossroad_choice == "right":
    print("You fell into a hole. Game over!")
elif crossroad_choice == "left":
    swim_choice = input('''You've come to a lake. There is an island in the middle of the lake.
            Type "wait" to wait for a boat. Type "swim" to swim across.
''').lower()
    if swim_choice == "swim":
        print("You get attacked by an angry trout. Game Over!")
    elif swim_choice == "wait":
        door_choice = input('''You arrive at the island unharmed. There is a house with 3 doors.
            Red, yellow and blue. Which color do you choose?
''').lower()
        if door_choice == "red":
            print('''It's a room full of fire. Game Over!''')
        elif door_choice == "yellow":
            print('''You found the treasure. You win!''')
        elif door_choice == "blue":
            print('''You enter a room of beasts. Game Over!''')
        else:
            print('''Red, yellow or blue. Game Over!''')
    else:
        print("Swim or wait. Try again.")
else:
    print("Left or right. Try again.")