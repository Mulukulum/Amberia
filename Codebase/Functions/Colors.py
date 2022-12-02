from random import choice
Colors=[1921186, 
        5646127, 
        8069048, 
        9201120, 
        2768197, 
        5177211,
        432432, 
        13419293, 
        16729344, 
        16249827]
def GetRandomColor():
    return choice(Colors)       #Returns a random Color from the list
def HexFormat(number: int) -> str:
    number=abs(number)          #Line to ensure someone that negative values don't mess stuff up
    if number>=16777214:        #If the number is too big just return White
        return  "#FFFFFF"
    #This next bit takes the hex value and removes the starting 0x bit added by python
    #Uppercase that and make it have a length of 6 using the .rjust() method
    hexcode=hex(number)[2::].upper().rjust(6,"0")       
    return "#"+hexcode
