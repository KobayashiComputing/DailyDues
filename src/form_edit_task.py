import FreeSimpleGUI as sg
from helpers import *
from task import *
from datetime import datetime, timedelta

def editTaskForm(task, taskList):
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

    # first, save the original task's data in dictionary format:
    freqCurrent = freqList[task.frequency.value - 1]
    priorityCurrent = priorityList[task.priority - 1]
    targetCurrent = task.target.total_seconds() / 3600

    # All the stuff inside the window.
    layout = [
        [sg.Text('Edit Task - all fields are required')],
        [sg.Push(), sg.Text('Name'), sg.InputText(default_text=task.name, key='name')],
        [sg.Push(), sg.Text('Description'), sg.InputText(default_text=task.description, key='description')],
        [sg.Push(), sg.Text('Target (hours per period)'), sg.InputText(default_text=f'{targetCurrent}', key='target')],
        [sg.Push(), sg.Text('Next Reset Date'), sg.InputText(default_text=task.reset.strftime("%Y-%m-%d %H:%M:%S")
, key='reset')],
        [
            sg.Push(),
            sg.Text('Frequency'), sg.Listbox(freqList, default_values=[freqCurrent], size=(13, 5), select_mode="LISTBOX_SELECT_MODE_SINGLE", key='frequency')
        ],

        [sg.CalendarButton('Use Date Picker', close_when_date_chosen=True, target='reset', no_titlebar=False), sg.Cancel(), sg.Save()]
    ]

    # newTask will be our return value, set it up here in case we get a 'Cancel'
    # or 'WIN_CLOSED' event
    newTask = None

    # Create and show the Window
    form_edit_task = sg.Window('Task', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = form_edit_task.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        # the only non-exit button click is the 'Save' button, so handle that here
        # 'values' is a dictionary with field names and data
        # print('You entered ', values)

        if event == "Save":
            # Check to make sure all fields are filled in...
            if values['name'] == "" or values['description'] == "" or values['target'] == "" or values['frequency'] == "" or values['reset'] == "":
                displayErrorDialog("All fields must be filled in with appropriate values.")
                continue
            elif isDuplicateTask(values['name'], taskList) and values['name'] != task.name:
                displayErrorDialog(f'A task with the name "{values['name']}" already exists. Please choose another name...')
                continue
            elif not validate_datetime_format(values['reset']):
                displayErrorDialog(f'Reset datetime format is not valid. It should be in the format "YYYY-MM-DD HH:MM:SS"...')
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
                # values['priority'] = str(priorityList.index(values['priority'][0]) + 1)
                values['priority'] = "3"
                values['target'] = str(timedelta(hours=float(values['target'])))

                # Next, we need to add the non-editable fields from the original task
                values['created'] = task.created.strftime("%Y-%m-%d %H:%M:%S")
                values['duration_total'] = str(task.duration_total)
                values['duration_period'] = str(task.duration_period)
                values['duration_session'] = str(task.duration_session)
                values['dtg_session_start'] = task.dtg_session_start
                values['dtg_session_paused'] = task.dtg_session_paused
                values['dtg_session_stop'] = task.dtg_session_stop
                # values['reset'] = task.reset.strftime("%Y-%m-%d %H:%M:%S")

                newTask = Task.newTaskFromDictionary(values)
                break

    form_edit_task.close()
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

