# def is_leap_year(year):

#     if(year %4 == 0):
#         if(year %100 ==0):
#             if(year %400 ==0):
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# print(is_leap_year(2020)) 

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))