dirty_dozen = ["Strawberries","Spinach", "Kale","Nectarines","Apples","Grapes","Peaches","Cheeries","Pears","Tomatoes","Celery","Potatoes"]

fruits = ["Strawberries","Apples","Grapes","Cheeries","Pears","Nectarines","Peaches"]
vegetables = ["Spinach","Kale","Tomatoes","Celery","Potatoes"]

dirty_fruits = []
dirty_vegetables = []

for item in dirty_dozen:
    if item in fruits:
        dirty_fruits.append(item)
    elif item in vegetables:
        dirty_vegetables.append(item)
print(dirty_fruits)
print(dirty_vegetables)            
