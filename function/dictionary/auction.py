biding = {}
highest_biding_amout = 0
other_bider = True
winner = ""
while other_bider == True:
    name = str(input("What is your name? "))
    bid = int(input("What is your bid? : $"))
    biding[name] = bid
    other = str(input("Are there any other bidders? Type 'yes' or 'no'. ").lower())
    if(other == "no"):
        other_bider = False    
    elif (other != "yes" and other != "no"):
        print("Please Answer is 'yes' or 'no'. ")


    for key in biding: 
            if(highest_biding_amout < biding[key]):
                highest_biding_amout = biding[key]
                winner = key
    print(f"The Winner is {winner} with a bid of ${highest_biding_amout}")               









# biding = {"Siddharth": 120}
# for key in biding:
#     print(f"Biding amount is {biding[key]}")

