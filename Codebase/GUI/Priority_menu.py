import PySimpleGUI as sg
sg.theme('Dark Amber')
a=[x for x in range(1,11)]
b=['#FA3E45','#F53795','#7B1FB8','#8C65E0','#22E8B9','#4EFF7B','#699930','#CCC31D','#FF4500','#F7F3E3']
layout = [[sg.Button(f"{A}",button_color=f"{b[A-1]}")] for A in a]

win=sg.Window("Dropdown Box", layout)
e,v=win.read()
win.close()
priority_no=e
sg.popup("Priority Chosen:", priority_no)