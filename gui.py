import PySimpleGUI as sg

layout = [
    [sg.B("Auglis", button_color="red")],
    [sg.B("Dārzenis", button_color="orange")]
]

window = sg.Window("My app",layout)
event, values = window.read()
if event == "Auglis":
    sg.popup("Kāds Auglis?")
elif event == "Dārzenis":
    sg.popup("Kāds Dārzenis?")

print(event, values)