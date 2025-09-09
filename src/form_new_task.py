import FreeSimpleGUI as sg
from task import *


def newTaskForm():
    # sg.theme('Dark')   # theme for this window, or all of sg?
    # All the stuff inside your window.
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    form_new_task = sg.Window('Task', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = form_new_task.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    form_new_task.close()

