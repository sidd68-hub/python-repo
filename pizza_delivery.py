print("Welcom to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Please Enter Valid Size")
if size == "S" and pepperoni == "Y":
    bill +=2
if (size == "M" or size == "L") and pepperoni =="Y":
    bill +=3    
else:
    print("Please Enter Valid Output")
if(extra_cheese == "Y"):
    bill +=1
    print(f"Your total bill is ${bill}")
else:
     print(f"Your total bill is ${bill}")           




