import random

user_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_value = random.randint(0,2)
print(f"Computer choose {computer_value}")
 
if user_value >=3 or computer_value <0:
    print("You typed an invalid number. You Lose")
elif user_value == 0 and computer_value == 2:
    print("You Win!")
elif computer_value == 0 and user_value == 2:
    print("You Lose! ")    
elif computer_value > user_value:
    print("You Lose!")
elif user_value > computer_value:
    print("You Win!")     
elif computer_value == user_value:
    print("It's a Draw")           
                                       