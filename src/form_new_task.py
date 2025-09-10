import FreeSimpleGUI as sg
from task import *


def newTaskForm():
    # sg.theme('Dark')   # theme for this window, or all of sg?
    freqList = [
        "Daily",
        "Weekday",
        "Weekly",
        "Work Weekly",
        "Bi-weekly",
        "Monthly",
        "Quarterly",
        "Bi-annually",
        "Annually"
    ]

    priorityList = [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]

    # All the stuff inside your window.
    layout = [
        [sg.Text('New Task - Name and Description are required')],
        [sg.Text('Priority defaults to 3 and Frequency to Daily')],
        [sg.Push(), sg.Text('Name'), sg.InputText(key='name')],
        [sg.Push(), sg.Text('Description'), sg.InputText(key='description')],
        [
            sg.Push(),
            sg.Text('Frequency'), sg.Listbox(freqList, default_values=["Daily"], select_mode="LISTBOX_SELECT_MODE_SINGLE", key='frequency'),
            sg.Text('          '),
            sg.Text('Priority'), sg.Listbox(priorityList, default_values=["3"], select_mode="LISTBOX_SELECT_MODE_SINGLE", key='priority'),
            sg.Text('                       ')
        ],
        [sg.Save(), sg.Cancel()]
    ]

    # Create the Window
    form_new_task = sg.Window('Task', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = form_new_task.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values)

    form_new_task.close()

