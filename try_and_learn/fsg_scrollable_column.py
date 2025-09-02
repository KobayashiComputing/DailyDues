import FreeSimpleGUI as sg

# Define the layout with a scrollable Column
layout = [
    [sg.Text("Resizable Window with Scrollbar Example")],
    [sg.Column(
        [[sg.Text(f"Item {i}")] for i in range(1, 101)],  # Example content
        size=(300, 400),  # Fixed size for the scrollable area
        scrollable=True,
        vertical_scroll_only=True
    )]
]

# Create the window
window = sg.Window("Resizable Window with Scrollbar", layout, resizable=True)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
