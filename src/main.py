import sys
import FreeSimpleGUI as sg
import subprocess
import os
from task import *

ROOT_PATH = './'

def Launcher():

    sg.theme('Dark')
    sg.set_options(element_padding=(2, 2),
        button_element_size=(25, 2), auto_size_buttons=False)
    
    taskList = testTaskList()
    buttonStack = []
    for task in taskList:
        buttonStack.append([sg.Button(f'{task.name} (P:{task.priority})', button_color=('white', '#35008B'))])
    
    buttonStack.append([sg.Button('EXIT', button_color=('white', 'firebrick3'))])

    layout = [ buttonStack ]

#     layout = [
# #        [sg.Combo(values=namesonly, size=(35, 30), key='demofile'), sg.Button('Run', button_color=('white', '#00168B'))],
#                [sg.Button('Task 1', button_color=('white', '#35008B'))],
#                [sg.Button('Task 2', button_color=('white', '#35008B'))],
#                [sg.Button('Task 3', button_color=('white', '#35008B'))],
#                [sg.Button('EXIT', button_color=('white', 'firebrick3'))],
# #              [sg.Text('', text_color='white', size=(50, 1), key='output')]]
#     ]

    window = sg.Window('Daily Dues',
                       layout,
                       no_titlebar=False,
                       grab_anywhere=True,
                       keep_on_top=True)

    # ---===--- Loop taking in user input and executing appropriate program --- #
    while True:
        event, values = window.read()
        if event == 'EXIT' or event == sg.WIN_CLOSED:
            break           # exit button clicked
        if event == 'Task 1':
            print('Run your program 1 here!')
        elif event == 'Task 2':
            print('Run your program 2 here!')
        elif event == 'Task 3':
            print('Run your program 3 here!')
        elif event == 'Demo':
            file = values['']
            print(f"Launching {event} '{values}'")
        else:
            print(f"Unhandled event '{event}'")

    print(f"Ending program based on button press: 'event' is '%{event}' and 'values' is '%{values}'")
    window.close()


if __name__ == '__main__':
    Launcher()
