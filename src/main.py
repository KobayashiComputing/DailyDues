import sys
import FreeSimpleGUI as sg
import subprocess
import os
from task import *

ROOT_PATH = './'

def show_button_stack(b):
    layout = [ b ]
    window = sg.Window( 'Daily Dues',
                        layout,
                        no_titlebar=False,
                        grab_anywhere=True,
                        keep_on_top=True)
    return window 


def Launcher():

    sg.theme('Dark')
    sg.set_options(element_padding=(2, 2),
        button_element_size=(25, 2), auto_size_buttons=False)
    
    taskList = testTaskList()
    buttonStack = []
    for task in taskList:
        buttonStack.append([sg.Button(f'{task.name} (P:{task.priority})', button_color=Task.task_color_pairs[task.state.value], key=task.name)])  
    buttonStack.append([sg.Button('EXIT', button_color=('white', 'firebrick3'))])

    window = show_button_stack(buttonStack)

    # Main loop... repeat until window is closed or "Exit" is clicked...
    while True:
        event, values = window.read()

        if event == 'EXIT' or event == sg.WIN_CLOSED:
            print(f"Ending program based on button press: 'event' is '%{event}' and 'values' is '%{values}'")
            clean_up_for_exit()
            break           # exit button clicked

        print(f"Button for '{event}' clicked...")
        for index, task in enumerate(taskList):
            if task.name in event:
                print(f"Found '{task.name}' at index: {index}")
                newTask = taskList[index]
                break

        oldTask = Task.get_current_task()
        newTask = newTask.change_task_state()
        if newTask == None:     # the old task was simply 'paused'
            window[oldTask.name].update(button_color=Task.task_color_pairs[oldTask.state.value])
        
        elif newTask == oldTask:    # the old task was restarted
            window[oldTask.name].update(button_color=Task.task_color_pairs[oldTask.state.value])

        else:   # a new task was started
            if oldTask != None:
                window[oldTask.name].update(button_color=Task.task_color_pairs[oldTask.state.value])
            if newTask != None:
                window[newTask.name].update(button_color=Task.task_color_pairs[newTask.state.value])

    # We've exited the loop, so close the window and clean up...
    window.close()


if __name__ == '__main__':
    Launcher()
