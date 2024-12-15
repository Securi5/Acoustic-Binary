global number
string = str(input("input string"))


def createFrame(character):
    frame = "10" #every frame starts with a start bit which is "1"
    binary = bin(ord(character))[2:]
    frame += (8 - len(binary)) * "0" + binary #adds the 7 bits corresponding the the ASCII value of the character to the frame and pads with zeros at the beggining so there is always 8 data bits
    if binary.count("1") %2 == 0: #adds a parity bit where the if the number of "1"s in the data bits is even then the parity bit is "0" if its odd its "1"
        frame += "0"
    else:
        frame += "1"
    frame += "0" #adds stop bit to the end "0"
    print(frame)

def sortString(string):
    number = ""
    for i, char in enumerate(string):
        if i == len(string) - 1 and char.isdigit() == True: #if character is the last character in the string is a number then:
            number += char #add character to number variable
            #create frame for that number
            createTransmittableNumberChunk(number)
            number = ""
        if i == len(string) - 1 and char.isdigit() == False:
            if number != "":
                createTransmittableNumberChunk(number)
                number = ""
                #create frame for number
            createFrame(char)
        if i != len(string) - 1 and char.isdigit() == True:
            number += char
        if i != len(string) - 1 and char.isdigit() == False:
            if number != "":
                createTransmittableNumberChunk(number)
                #create number frame
                number = ""
            createFrame(char)

def createTransmittableNumberChunk(number):
    numberChunk = ""
    for i, char in enumerate(number):
        if i == len(number) - 1 and int(numberChunk + char) > 255:
            createNumberFrame(numberChunk)
            numberChunk = char
            createNumberFrame(numberChunk)
        elif i == len(number) - 1 and int(numberChunk + char) <= 255:
            numberChunk += char
            createNumberFrame(numberChunk)
        elif i != len(number) - 1 and int(numberChunk + char) > 255:
            createNumberFrame(numberChunk)
            numberChunk = char
        elif i != len(number) - 1 and int(numberChunk + char) <= 255:
            numberChunk += char

def createNumberFrame(numberChunk):
    frame = "11"
    binary = bin(int(numberChunk))[2:]
    frame += (8 - len(binary)) * "0" + binary
    if binary.count("1") %2 == 0:
        frame += "0"
    else:
        frame += "1"
    frame += "0"
    print(frame)
                   
            
sortString(string)