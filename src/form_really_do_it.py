import FreeSimpleGUI as sg
from task import *

def really_do_it(msgString):
    # The layout for the FreeSimpleGUI window.
    layout = [
        [sg.Text(msgString)],
        [sg.Yes(), sg.No()]
    ]

    doIt = False

    # Create and show the Window
    form_really_do_it = sg.Window('Really do this?', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = form_really_do_it.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            doIt = False
            break

        if event == "Yes":
            doIt = True
            break

        if event == "No":
            doIt = False
            break
        
    form_really_do_it.close()
    return doIt

