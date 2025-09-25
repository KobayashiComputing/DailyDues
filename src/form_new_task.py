import FreeSimpleGUI as sg
from helpers import *
from task import *
from datetime import datetime, timedelta

def newTaskForm(taskList):
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
        [sg.Push(), sg.Text('Target (hours per period)'), sg.InputText(key='target')],
        [
            sg.Push(),
            sg.Text('Frequency'), sg.Listbox(freqList, default_values=["Daily"], size=(13, 5), select_mode="LISTBOX_SELECT_MODE_SINGLE", key='frequency'),
            sg.Text('          '),
            sg.Text('Priority'), sg.Listbox(priorityList, default_values=["3"], size=(3, 5), select_mode="LISTBOX_SELECT_MODE_SINGLE", key='priority'),
            sg.Text('                       ')
        ],
        [sg.Save(), sg.Cancel()]
    ]

    # newTask will be our return value, set it up here in case we get a 'Cancel'
    # or 'WIN_CLOSED' event
    newTask = None

    # Create and show the Window
    form_new_task = sg.Window('Task', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = form_new_task.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        # the only non-exit button click is the 'Save' button, so handle that here
        # 'values' is a dictionary with field names and data
        # print('You entered ', values)

        if event == "Save":
            # Check to make sure all fields are filled in...
            if values['name'] == "" or values['description'] == "" or values['target'] == "" or values['frequency'] == "" or values['priority'] == "":
                displayErrorDialog("All fields must be filled in with appropriate values.")
                continue
            elif isDuplicateTask(values['name'], taskList):
                displayErrorDialog(f'A task with the name "{values['name']}" already exists. Please choose another name...')
                continue
            else:
                # Convert the 'frequency' and 'priority' into values that the Task.newTaskFromDictionary()
                # can process...
                # Note:
                #   - FreeSimpleGUI Listbox element returns a list
                #   - We need to add 1 to the index because the list is zero-bassed
                #   - Then convert the index to a string, because that's what Task.newTaskFromDictionary()
                #     expects
                #
                fNdx = freqList.index(values['frequency'][0]) + 1
                eName = next((member.name for member in ResetFrequency if member.value == fNdx), 'DAILY')
                values['frequency'] = f"ResetFrequency.{eName}"
                values['priority'] = str(priorityList.index(values['priority'][0]) + 1)
                values['target'] = str(timedelta(hours=float(values['target'])))

                # Next, we need to add the other Task fields to the dictionary
                values['created'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                values['duration_total'] = "0.0"
                values['duration_session'] = "0.0"
                values['duration_period'] = "0.0"
                values['dtg_session_start'] = "None"
                values['dtg_session_paused'] = "None"
                values['dtg_session_stop'] = "None"
                # the 'reset' will be calculated in the 'newTaskFromDictionary()' function.
                # If it's 'None', it will be based on 'created' and 'frequency'.
                values['reset'] = None

                newTask = Task.newTaskFromDictionary(values)
                break


    form_new_task.close()
    return newTask


# Some example code I thought might be useful at some point...
#-----[ populate sg.listbox from enum ]-----

# import PySimpleGUI as sg
# from enum import Enum

#-----[ populate sg.listbox from enum ]-----
# # Define an Enum
# class Colors(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3
#     YELLOW = 4

# # Extract Enum names or values
# enum_names = [color.name for color in Colors]  # ['RED', 'GREEN', 'BLUE', 'YELLOW']
# # enum_values = [color.value for color in Colors]  # [1, 2, 3, 4] (if you prefer values)

# # Define the layout with a Listbox
# layout = [
#     [sg.Text("Select a color:")],
#     [sg.Listbox(values=enum_names, size=(20, len(enum_names)), key='-LISTBOX-')],
#     [sg.Button("Submit"), sg.Button("Exit")]
# ]

# # Create the window
# window = sg.Window("Enum to Listbox Example", layout)

# # Event loop
# while True:
#     event, values = window.read()
#     if event in (sg.WINDOW_CLOSED, "Exit"):
#         break
#     elif event == "Submit":
#         selected = values['-LISTBOX-']
#         sg.popup(f"You selected: {selected}")

# # Close the window
# window.close()
#-----[ end: populate sg.listbox from enum ]-----

