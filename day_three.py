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
print("You are travelling through the winds on a cold snowy night.")
print("The path has become obscured and you've lost your way.")
print("A fork appears ahead, which way will you go?")
direction = input("Type 'Left' or 'Right': ")

if direction == "Right" or direction == "right":
  print("The path becomes slippery and you fall off a cliff.")
else:
  print("Your path becomes clearer, you can see it has been travelled recently.")

  print("As you trudge ahead you hear the sound of running water.")
  print("Slowly a river appears in the distance.")
  print("The path ends on the river's edge, the water is high and moving fast.")
  print("Do you cross now or wait for the water to recede?")
  cross = input("Type 'Cross' or 'Wait': ")
  
  if cross == "Cross" or cross == "cross":
    print("The water is too swift, you are swept away.")
  else:
    print("You wait for the water to go down and find a safe crossing.")
  
    print("The storm clears as night ends. A crumbling fortress looms in the foggy morning.")
    print("Inside the fortress you are travelling down a long hallway, 3 doors appear at the end.")
    print("The doors are painted red, yellow, and blue. Which door do you choose?")
    door = input("Type 'Red', 'Yellow', or 'Blue': ")
    if door == "Yellow" or door == "yellow":
      print("You open the door, a warm glow filling your view.")
      print("Treasure fills the room from wall to wall in glistening piles.")
      print("You Win!")
    else:
      print("It is pitch black inside the room. You slowly creep forward.")
      print("The floor falls away beneath your feet, and you fall endlessly into the darkness.")
      print("You Lose.")