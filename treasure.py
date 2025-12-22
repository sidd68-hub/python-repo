print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure ")
direction = input("You're at a cross road. Where do you want to go?\nType left or right: ")
if(direction == "right"):
    print("Game over")
elif direction == "left" :
    travel = input("You've come to a lake. There is an island in the middle of the lake.\nType wait to wait for a boat. Type swim to swim across. ")
    if travel == "swim":
     print("Game Over") 
    else:
     color = input("You arrive at the island unharmed. There is house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose? ")
     if(color == "red" or color =="blue"):
        print("Game Over")
     else:
        print("You Win!")   
else:
    print("Please enter Valid Direction ")       
