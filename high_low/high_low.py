import random
import data


# #1 create print statement
# choice_a, choice_b = random.sample(data.data,2)
# print(f'Compare A: {choice_a['name']}, {choice_a['description']}, {choice_a['country']}\n\n')
# print("VS\n\n")
# print(f'Compare B: {choice_b['name']}, {choice_b['description']}, {choice_b['country']}\n\n')
# answer = str(input("Who has more followers? Type 'A' or 'B' : "))

# if answer == "A":
#     if(choice_a["follower_count"] > choice_b["follower_count"]):
#         print("Win")
#     else:
#         print("Lose")
# else:
#     if(choice_b["follower_count"]> choice_a["follower_count"]):
#         print("Win")
#     else:
#         print("Lose")          
# 

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess =="a"
    else:
        return user_guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data.data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data.data)
    if account_a == account_b:
        account_b = random.choice(data.data)

    print(f"Compare A: {format_data(account_a)}.\n")
    print("vs\n")
    print(f"Compare B: {format_data(account_b)}.\n")    


    guess = str(input("Who has more followers? Type 'A' or 'B' : ").lower())


    a_follower_account  = account_a["follower_count"]
    b_follower_account  = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_account,b_follower_account)

    if is_correct:
        score +=1
        print(f"You're right! Current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {score}")

           








#2 Take Output
#3 make a array and pick random name
#4 take input of answer
#5 compare the answer
#6 End game