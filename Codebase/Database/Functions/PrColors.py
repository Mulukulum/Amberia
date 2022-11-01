from Codebase.Database.Initialize import AttribDict 
Colors={
    1:16399941,
    2:16070549,
    3:8069048,
    4:9201120,
    5:2287801,
    6:5177211,
    7:432432,
    8:13419293,
    9:16729344,
    10:16249827,
}

def DefaultColor(con):
    for ClrLevel,ColorCode in Colors:                                 
        con.execute(f"""DELETE * FROM colors;""")                     #Clears the table of any values
        con.execute(f"""INSERT INTO colors ({AttribDict['colors']}) VALUES (?,?);""",(ClrLevel,hex(ColorCode).upper())) #And inserts default values

