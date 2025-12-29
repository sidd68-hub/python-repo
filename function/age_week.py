def life_in_weeks(age,location):
    total_life_span = 90
    total_life_span -= age
    weeks = total_life_span * 52
    print(f"You have {weeks} weeks left, in {location}")


age = int(input("Enter Your age "))
location = input("Enter your location ")
print(age)
life_in_weeks(age=age,location=location)
