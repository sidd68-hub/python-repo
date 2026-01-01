total = 0.0

def add(a,b):
   return a + b

def subtract(a,b):
    return a - b    

def multiple(a,b):
    return a*b  

def division(a,b):
    if(b == 0):
        print("Cannot divide by Zero.")
        return None
    return a/b

operation = {
    '*': multiple,
    '/':division,
    '+':add,
    '-':subtract,
}
def calculator():
        should_accumulate = True

        num1 = float(input("What is the first number?: "))
        
        while should_accumulate: 
            
            for symbol in operation:
                print(symbol)
            operator = input("Pick an Symbol: ")
            num2 = float(input("What is the second number?: "))
            answer = operation[operator](num1,num2)
            print(f"{num1} {operator} {num2} = {answer}")
            choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. ").lower()     
            if choice == "y":
                num1 = answer
            else:
                should_accumulate = False
                print("\n" *  20)
                calculator()

calculator()                   
     

 