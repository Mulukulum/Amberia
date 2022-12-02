from random import choice
Colors=[1921186, #1D50A2
        5646127, #56272F
        8069048, #7B1FB8
        9201120, #8C65E0
        2768197, #2A3D45
        5177211, #4EFF7B
        432432, #069930
        13419293, #CCC31D
        16729344, #FF4500
        16249827] #F7F3E3

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
