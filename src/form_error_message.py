import FreeSimpleGUI as sg
from task import *

def error_message_dialog(msgString):
    # The layout for the FreeSimpleGUI window.
    layout = [
        [sg.Text(msgString)],
        [sg.Push(), sg.Ok()]
    ]

    gotIt = False

    # Create and show the Window
    form_error_message = sg.Window('Oops! There\'s a problem...', layout, modal=True)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = form_error_message.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            gotIt = False
            break

        if event == "Ok":
            gotIt = True
            break

    form_error_message.close()
    return gotIt

