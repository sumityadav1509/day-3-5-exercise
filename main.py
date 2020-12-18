print("Welcome to treasure island your mission is to find the treasure")  
choice1=input('You are at a crossroad , where do you wnat to go ? Type "Left" or "Right"').lower()  
if choice1=="left": 
  choice2=input('You have come to a lake.There is an island in the middle of the lake.Type "wait" to wait for a boat.Type"swim" to swim across').lower() 
  if choice2=="wait":
   choice3=input('You have arrived at the island unharmed.There is a house with 3 doors.One red , one yellow and one blue.Which color do you choose?').lower() 
    if choice3=="red": 
     print("It's a room full of fire. Game Over !")
    elif choice3=="blue":
      print("You have entered a room full of beasts. Game over ! ")
    elif choice3=="yellow":
       print("You found the Treasure!.You win")
    else: 
      print("You chose a door that doesn't exist . Game Over!") 
  else:
    print("You got attacked by an angry Shark.Game over")
else:
  print("Game Over you fell in to a hole !")


