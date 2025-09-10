import FreeSimpleGUI as sg
from task import *
from form_new_task import *
from commandline import *
from database import *

ROOT_PATH = './'

# Global vars used in this source file
dbCursor = None     # 
dbConn = None       #
dbVersion = None    # this will be a string

def show_button_stack(b):
    menu_def = [       # the "!" at the beginning of the menu item name makes it grayed out
        ['&File', ['Backup', ['Export', 'Import'], ['Save Database', 'Save Database As...', 'New Empty Database', 'New Test Database', 'E&xit']]],
        ['View', ['Summary', 'Details']],
        ['&Task', ['&New', 'Edit', 'Archive', 'Delete']],
        ['&Help', ['Docs', '&About...']]
    ]
    
    if len(b) < 12:
        scrollIt = False
    else:
        scrollIt = True

    layout = [ 
        [sg.Menu(menu_def, key='MainMenu')],
        # give the column element a 'key' so that it can be updated later... hopefully...
        [sg.Column(b, scrollable=scrollIt, vertical_scroll_only=True, key='ButtonColumn')],
        [sg.Button('EXIT', button_color=('white', 'firebrick3'), key='EXIT')]
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

    # NOTE: only one of the 'taskList =' lines should be uncommented. Choose
    # which one based on the comments...
    #
    # load the task list from the database...
    taskList = Task.getTaskList(dbCursor)
    # ...or generate one 
    # taskList = testTaskList(13)

    buttonStack = []
    for task in taskList:
        buttonStack.append([sg.Button(f'{task.name} (P:{task.priority})', button_color=Task.task_color_pairs[task.state.value], key=task.name)])  
    

    window = show_button_stack(buttonStack)

    # Main loop... repeat until window is closed or "Exit" is clicked...
    while True:
        event, values = window.read()

        # find out if we need to exit ('Exit' button or the window's 'X')
        if event == 'EXIT' or event == 'Exit' or event == sg.WIN_CLOSED:
            # print(f"Ending program based on button press: 'event' is '%{event}' and 'values' is '%{values}'")
            Task.clean_up_for_exit()
            break           # exit button clicked

        # okay, so not exiting; find out if the 'event' was one of our task buttons...
        isTaskButton = False
        for index, task in enumerate(taskList):
            if task.name == event:
                # print(f"Found '{task.name}' at index: {index}")
                newTask = taskList[index]
                isTaskButton = True
                break
        
        if isTaskButton:
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
        else:
            # if it wasn't an exit event, and not a task button, hopefully it's a menu selection
            match event:
                # The 'File' submenu...
                case "Export":
                    pass
                case "Import":
                    pass
                case "Save Database":
                    pass
                case "Save Database As...":
                    pass
                case "New Empty Database":
                    pass
                case "New Test Database":
                    pass
                case "Exit":
                    pass

                # The 'View' submenu...
                case "Summary":
                    pass
                case "Details":
                    pass

                # The 'Task' submenu...
                case "New":
                    newTask = newTaskForm()
                    if newTask != None:
                        pass
                    pass
                case "Edit":
                    pass
                case "Archive":
                    pass
                case "Delete":
                    pass

                # The 'Help' submenu
                case "Docs":
                    pass
                case "About...":
                    pass
                case _:
                    print(f"Hmmm... the '{event}' button was pressed...")


    # We've exited the event loop, so close the window and clean up...
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
    print(f"Using database file {dbname}")
    ConnectDB(dbname)
    DailyDues()
