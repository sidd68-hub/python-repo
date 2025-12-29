alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
    output_text = ""
    if direction == "decode":
       shift *= -1
       
    for letter in text.lower():
       if letter not in alphabet:
           output_text += letter
       else:
          shifted_position = alphabet.index(letter) + shift
          shifted_position %= len(alphabet)
          output_text += alphabet[shifted_position]
    print(f"Here is the result: {output_text}")    

should_continue = True

while should_continue == True:
    direction_type = str(input("Please enter Encoded type "))
    text = str(input("Enter Text here "))
    shift = int(input("Enter number to be shifted "))
    caesar(direction=direction_type,text=text,shift=shift)
    restart =input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if restart == "no":
        should_continue = False