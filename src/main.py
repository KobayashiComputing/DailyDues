import FreeSimpleGUI as sg
from task import *
from commandline import *
from database import *

ROOT_PATH = './'

# Global vars used in this source file
dbCursor = None     # 
dbConn = None       #
dbVersion = None    # this will be a string

def show_button_stack(b):
    if len(b) < 12:
        b.append([sg.Button('EXIT', button_color=('white', 'firebrick3'))])
        layout = [ b ]
    else: 
        layout = [
            [sg.Column(b, scrollable=True, vertical_scroll_only=True)],
            [sg.Button('EXIT', button_color=('white', 'firebrick3'))]
        ]

    window = sg.Window( 'Daily Dues',
                        layout,
                        no_titlebar=False,
                        grab_anywhere=True,
                        keep_on_top=True,
                        resizable=False, 
                        finalize=True)

    # window.set_resizable(False, True)
    return window 


def DailyDues():

    sg.theme('Dark')
    sg.set_options(element_padding=(2, 2),
                   button_element_size=(25, 2), 
                   auto_size_buttons=False)
    
    pass

    taskList = Task.getTaskList(dbCursor)
    # taskList = testTaskList(13)
    buttonStack = []
    for task in taskList:
        buttonStack.append([sg.Button(f'{task.name} (P:{task.priority})', button_color=Task.task_color_pairs[task.state.value], key=task.name)])  
    

    window = show_button_stack(buttonStack)

    # Main loop... repeat until window is closed or "Exit" is clicked...
    while True:
        event, values = window.read()

        if event == 'EXIT' or event == sg.WIN_CLOSED:
            # print(f"Ending program based on button press: 'event' is '%{event}' and 'values' is '%{values}'")
            Task.clean_up_for_exit()
            break           # exit button clicked

        # print(f"Button for '{event}' clicked...")
        for index, task in enumerate(taskList):
            if task.name == event:
                # print(f"Found '{task.name}' at index: {index}")
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
    saveTasksTable(taskList)
    closeDB()
    window.close()

def ConnectDB(dbname):
    global dbConn
    global dbCursor
    dbConn, dbCursor, dbEmpty = dbGetDatabaseCursor(dbname)
    if dbEmpty:
        # print(f"Database {dbname} is empty! (Probably just created...)")
        dbVersion = dbInitDatabase(dbCursor)
        dbCommit(dbConn)
        print(f"Database {dbname} initialized to version {dbVersion}")

def saveTasksTable(taskList):
    for task in taskList:
        task.saveToDatabase(dbCursor)

def closeDB():
    global dbConn
    dbSaveDatabase(dbConn)

if __name__ == '__main__':
    dbname = cliGetDatabaseName()
    # print(f"Using database file {dbname}")
    ConnectDB(dbname)
    DailyDues()
