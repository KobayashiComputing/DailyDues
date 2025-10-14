import FreeSimpleGUI as sg  # FreeSimpleGUI is based on PySimpleGUI

# Define the layout with formatted text
layout = [
    [sg.Text("Welcome to FreeSimpleGUI!", font=("Helvetica", 16), text_color="blue")],
    [sg.Text("This is an example of formatted text.", font=("Arial", 12), text_color="green")],
    [sg.Text("Enjoy creating GUIs!", font=("Courier", 14, "italic"), text_color="purple")],
    [sg.Button("OK")]
]

# Create the window
window = sg.Window("Formatted Text Example", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "OK":
        break

window.close()
