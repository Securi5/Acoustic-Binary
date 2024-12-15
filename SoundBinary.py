global number
string = input("input string")
number = []

def createFrame(character):
    frame = "1" #every frame starts with a start bit which is "1"
    binary = bin(ord(character))[2:]
    if character.isdigit() == True: #if the character is a digit then the heading bit is "1"
        frame += "1"
    else:
        frame += "0" #if the character is not a number then heading bit is "0"
    frame += (8 - len(binary)) * "0" + binary #adds the 7 bits corresponding the the ASCII value of the character to the frame and pads with zeros at the beggining so there is always 8 data bits
    if binary.count("1") %2 == 0: #adds a parity bit where the if the number of "1"s in the data bits is even then the parity bit is "0" if its odd its "1"
        frame += "0"
    else:
        frame += "1"
    frame += "0" #adds stop bit to the end "0"
    print(frame)
def createNumberFrame(number):
    print()

for i in string:
    if i.isdigit() == True:
        number.append(i)
    if i.isdigit() == False and number != []:
        createNumberFrame(number)
        number = []
        createFrame(i)
    if i.isdigit() == False and number == []:
        createFrame(i)
