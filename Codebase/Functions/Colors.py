from random import choice
Colors=(1921186, #1D50A2 (YInMn Blue)
        9508395, #56272F (Crimson Red)
        6047167, #5C45BF (Plump Purple)
        1533050, #17647A (Blue Sapphire)
        2648656, #4B8970 (Bottle Green)
        7887204, #785964 (Deep Taupe)
        11745549, #B3390D (Rust)
        4719445, #480355 (Russian Violet)
)

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
