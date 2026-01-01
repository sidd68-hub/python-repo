# tarvel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]    
# }
# print(tarvel_log["France"][1])

# nested_list = ["A", "B", ["C","D"]]
# print(f"Nested List is {nested_list[2][1]}") 

tarvel_log = {
    "France" : {
        "total_visits":8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "total_visits":2 ,
        "cities_visited":["Stuttgart", "Berlin"]  
    }  
}

print(tarvel_log["Germany"]["cities_visited"][0])

