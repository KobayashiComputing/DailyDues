import FreeSimpleGUI as sg
import copy
import json
from helpers import *
from task import *
from form_new_task import newTaskForm
from form_edit_task import editTaskForm
from commandline import *
from database import *
from form_ask_about_test_data import *
from form_really_do_it import *
from menu_help import *

ROOT_PATH = './'

# Settings dictionary, which will be stored in the database and recovered when 
# starting up
appSettings = {
    "currentView": "Summary",
    "possibleViewsNdx": 0,
    "winLocX": None,
    "winLocY": None,
    "appVersion": "0.00"
}

# Global vars used in this source file
appVersion = "0.00"
dbCursor = None     # 
dbConn = None       #
dbVersion = "0.10"    # this will be a string
dbEmpty = None
sgKeyNdx = 0
sgKeyList = ['0', '1', '2', '3', '4']
possibleViews = [
    ['Summary (Current)', 'Details'],
    ['Summary', 'Details (Current)']
]

def show_button_stack(taskList, location=(None, None)):
    global appSettings
    global possibleViews
    global sgKeyNdx, sgKeyList

    deleteTaskList = []
    editTaskList = []
    finishTaskList = []

    # increment the sgKeyNdx... do this here so that the global value is the same throughout this file
    sgKeyNdx = (sgKeyNdx + 1) %5
    
    # build the buttonStack with the sgKeyList[snKeyNdx] string appended to the key values of the buttons...
    # we need to do this to distinguish the buttons in this window from buttons in the 'old' window, which 
    # will be behind the new window when adding, deleting, or rearranging buttons in the stack.
    buttonStack = []
    for task in taskList:
        task.updateTaskState()
        if appSettings['currentView'] == "Details":
            buttonStack.append([sg.Button(f'{task.name}', 
                                        button_color=Task.task_color_pairs[task.state.value], 
                                        key=task.name+sgKeyList[sgKeyNdx]),
                                sg.Multiline(task.getTaskDetailsString(),
                                             key=task.name+"D"+sgKeyList[sgKeyNdx],
                                             size=(None, 2),
                                             no_scrollbar=True,
                                             write_only=True)
                                ])
        else:
            buttonStack.append([sg.Button(f'{task.name}', 
                                        button_color=Task.task_color_pairs[task.state.value], 
                                        key=task.name+sgKeyList[sgKeyNdx])])
            
        deleteTaskList.append(f'{task.name}::Delete')
        editTaskList.append(f'{task.name}::Edit')
        finishTaskList.append(f'{task.name}::Finish')

    if len(buttonStack) < 12:
        scrollIt = False
    else:
        scrollIt = True

    menu_def = [       # the "!" at the beginning of the menu item name makes it grayed out
        # ['&File', ['Backup', ['!Export', '!Import'], ['!Save Database', '!Save Database As...', '!New Empty Database', '!New Test Database', 'E&xit']]],
        ['&File', ['E&xit']],
        ['View', possibleViews[appSettings['possibleViewsNdx']]],
        # ['&Task', ['&New', 'Edit', editTaskList, '!Archive', 'Delete', deleteTaskList]],
        ['&Task', ['&New', 'Edit', editTaskList, 'Finish', finishTaskList, 'Delete', deleteTaskList]],
        ['&Help', ['User Guide', '&About...']]
    ]

    layout = [ 
        [sg.Menu(menu_def, key='MainMenu')],
        # [sg.Text(f'Current View: {appSettings['currentView']}')],
        [sg.Column(buttonStack, scrollable=scrollIt, vertical_scroll_only=True, key='ButtonColumn')],
        [sg.Button('EXIT', button_color=('white', 'firebrick3'), key='EXIT')]
    ]
    
    window = sg.Window( 'Daily Dues',
                        layout,
                        location=location,
                        no_titlebar=False,
                        grab_anywhere=True,
                        keep_on_top=False,
                        resizable=False, 
                        finalize=True)

    return window 

def update_main_window(oldWindow, taskList):
    update_settings_location(oldWindow)
    window = show_button_stack(taskList, location=oldWindow.current_location())
    oldWindow.close()
    return window

def update_settings_location(window):
    global appSettings
    appSettings['winLocX'] = window.current_location()[0]
    appSettings['winLocY'] = window.current_location()[1]
    saveAppSettings()
    return (appSettings['winLocX'], appSettings['winLocY'])

def update_task_details_pane(task, window):
    global sgKeyList, sgKeyNdx
    detailsString = task.getTaskDetailsString()
    eKey = task.name+"D"+sgKeyList[sgKeyNdx]
    window[eKey].update(detailsString)
    pass

def DailyDues():
    global sgKeyNdx, sgKeyList
    global dbCursor, dbVersion
    global currentView
    global appSettings
    global possibleViews

    sg.theme('Dark')
    sg.set_options(element_padding=(2, 2),
                   button_element_size=(25, 2), 
                   auto_size_buttons=False)
    
    pass

    # Check to see if the database is empty (newly created), and if it is, display a window 
    # to ask about creating 'test' data...
    # Note that this will work only for a *new* database, because once it's created, it's not
    # truly 'empty'
    # Note also that this is for use only while in early (more or less) development; it will 
    # be removed (probably) for production use.
    if dbEmpty:
        createTestData, testDataCount = askAboutTestData(dbname)
    else:
        createTestData = False
        testDataCount = 0

    if createTestData:
        taskList = testTaskList(testDataCount)
        saveTasksTable(taskList)
    else:
        taskList = Task.getTaskList(dbCursor)
    window = show_button_stack(taskList, location=(appSettings['winLocX'], appSettings['winLocY']))
    update_settings_location(window)
    bg_counter = 0

    # Main loop... repeat until window is closed or "Exit" is clicked...
    while True:
        # read any events from the window, but if idle for "x" seconds, run the 
        # housekeeping chores...
        # Note: the 'timeout' value is in milliseconds...
        #       1 second is 1000 milliseconds
        #       10 seconds is 10000 milliseconds
        #       1 minute is 60,000 milliseconds
        #       5 minutes is 300,000 milliseconds
        hkCycleTime = 60000     # 60 seconds, or 1 minute
        hkCycleTime = 30000     # 30 seconds
        hkCycleTime = 6000      # every 6 seconds, or .1 minutes
        event, values = window.read(timeout=hkCycleTime, timeout_key='--housekeeping--', close=False)
        pass

        if event == '--housekeeping--':
            bg_counter += 1
            # print(f'Housekeeping run # {bg_counter} (cycle time is {hkCycleTime/60000} minutes)...')
            update_settings_location(window)
            current_task = Task.get_current_task()
            if current_task != None:
                current_task.updateTaskDurations()
                if appSettings['currentView'] == "Details":
                    update_task_details_pane(current_task, window)

            # run 'updateTaskState()' for each task, and return true if any change was made
            # do this once per minute
            if (bg_counter % 10) == 0:
                for tTmp in taskList:
                    if tTmp.updateTaskState():
                        window[tTmp.name+sgKeyList[sgKeyNdx]].update(button_color=Task.task_color_pairs[tTmp.state.value])

            continue

        # find out if we need to exit ('Exit' button or the window's 'X')
        if event == 'EXIT' or event == 'Exit' or event == sg.WIN_CLOSED:
            # print(f"Ending program based on button press: 'event' is '%{event}' and 'values' is '%{values}'")
            Task.clean_up_for_exit()
            break           # exit button clicked

        # okay, so not exiting; find out if the 'event' was one of our task buttons...
        isTaskButton = False
        for index, task in enumerate(taskList):
            if task.name+sgKeyList[sgKeyNdx] == event:
                # print(f"Found '{task.name}' at index: {index}")
                newTask = taskList[index]
                isTaskButton = True
                break
        
        if isTaskButton:
            oldTask = Task.get_current_task()
            newTask = newTask.change_task_state()
            
            if appSettings['currentView'] == "Details" and oldTask != None:
                update_task_details_pane(oldTask, window)

            if newTask == None:     # the old task was simply 'paused'
                # window.find_element(oldTask.name+sgKeyList[sgKeyNdx], silent_on_error=True).Update(button_color=Task.task_color_pairs[oldTask.state.value])
                window[oldTask.name+sgKeyList[sgKeyNdx]].update(button_color=Task.task_color_pairs[oldTask.state.value])
            
            elif newTask == oldTask:    # the old task was restarted
                # window.find_element(oldTask.name+sgKeyList[sgKeyNdx], silent_on_error=True).Update(button_color=Task.task_color_pairs[oldTask.state.value])
                window[oldTask.name+sgKeyList[sgKeyNdx]].update(button_color=Task.task_color_pairs[oldTask.state.value])

            else:   # a new task was started
                if oldTask != None:
                    # window.find_element(oldTask.name+sgKeyList[sgKeyNdx], silent_on_error=True).update(button_color=Task.task_color_pairs[oldTask.state.value])
                    window[oldTask.name+sgKeyList[sgKeyNdx]].update(button_color=Task.task_color_pairs[oldTask.state.value])
                    if appSettings['currentView'] == "Details":
                        update_task_details_pane(oldTask, window)
                if newTask != None:
                    # window.find_element(newTask.name+sgKeyList[sgKeyNdx], silent_on_error=True).update(button_color=Task.task_color_pairs[newTask.state.value])
                    window[newTask.name+sgKeyList[sgKeyNdx]].update(button_color=Task.task_color_pairs[newTask.state.value])
                    if appSettings['currentView'] == "Details":
                        update_task_details_pane(newTask, window)
        else:
            # if it wasn't an exit event, and not a task button, hopefully it's a menu selection
            #
            # The 'Task' menu has two submenus - 'Edit' and 'Delete', and we need to determine if our event
            # is one of those...
            tmpNdx = event.find('::')
            if tmpNdx != -1:    # we have an edit, a finish, a delete, or a problem...
                tmpTaskID = event[:tmpNdx]
                event = event[tmpNdx+2:]
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
                case "Summary" | "Summary (Current)":
                    if appSettings['currentView'] != "Summary":
                        appSettings['currentView'] = "Summary"
                        appSettings['possibleViewsNdx'] = 0
                        window = update_main_window(window, taskList)                        

                case "Details" | "Details (Current)":
                    if appSettings['currentView'] != "Details":
                        currentView = "Details"
                        appSettings['currentView'] = "Details"
                        appSettings['possibleViewsNdx'] = 1
                        window = update_main_window(window, taskList)                        

                # The 'Task' submenu...
                case "New":
                    newTask = newTaskForm(taskList)
                    if newTask != None:
                        taskList.append(newTask)
                        newTask.saveToDatabase(dbConn, dbCursor)
                        window = update_main_window(window, taskList)

                case "Edit":
                    # print(f'Editing task "{tmpTaskID}"')
                    tmpNdx = next((i for i, obj in enumerate(taskList) if obj.name == tmpTaskID), -1)
                    if tmpNdx != -1:
                        newTask = editTaskForm(taskList[tmpNdx], taskList)
                        if newTask != None:
                            # if we changed the name (which is the main key for the task object and record),
                            # we need to delete the task with the old name from the database...
                            if newTask.name != taskList[tmpNdx].name:
                                dbDeleteTask(dbConn, dbCursor, 'tasks', taskList[tmpNdx])
                            taskList[tmpNdx] = newTask
                            newTask.saveToDatabase(dbConn, dbCursor)
                            window = update_main_window(window, taskList)
                    pass
                case "Finish":
                    # print(f'Finishing task "{tmpTaskID}"')
                    tmpNdx = next((i for i, obj in enumerate(taskList) if obj.name == tmpTaskID), -1)
                    if tmpNdx != -1:
                        msgString = f'Set task {taskList[tmpNdx].name} as "Finished" for its current reset period, which ends at {taskList[tmpNdx].reset}?'
                        if really_do_it(msgString):
                            taskList[tmpNdx].finish_task()
                    pass
                case "Delete":
                    # print(f'Deleting task "{tmpTaskID}"')
                    tmpNdx = next((i for i, obj in enumerate(taskList) if obj.name == tmpTaskID), -1)
                    if tmpNdx != -1:
                        # show dialog window to confirm delete...
                        if reallyDoIt(f'Really delete task "{taskList[tmpNdx].name}"? (This is immediately permanent!)'):
                            tmpTask = taskList.pop(tmpNdx)
                            dbDeleteTask(dbConn, dbCursor, 'tasks', tmpTask)
                            window = update_main_window(window, taskList)
                    pass

                # The 'Help' submenu
                case "User Guide":
                    app_user_guide()
                case "About...":
                    app_about(dbname, appSettings['appVersion'], dbVersion, sgKeyNdx, bg_counter, appSettings['currentView'])
                case _:
                    error_message_dialog(f"Hmmm... the '{event}' button was chosen...")
                    # print(f"Hmmm... the '{event}' button was chosen...")


    # We've exited the event loop, so close the window and clean up...
    saveTasksTable(taskList)
    saveAppSettings()
    closeDB()
    window.close()

def ConnectDB(dbname):
    global dbConn
    global dbCursor, dbVersion
    global dbEmpty
    dbConn, dbCursor, dbEmpty = dbGetDatabaseCursor(dbname)
    if dbEmpty:
        # print(f"Database {dbname} is empty! (Probably just created...)")
        dbVersion = dbInitDatabase(dbCursor)
        dbCommit(dbConn)
        error_message_dialog(f"'{dbname}' was not found, so it was created and initialized to version {dbVersion}")
        # print(f"Database {dbname} initialized to version {dbVersion}")
    else:
        dbVersion = dbGetDatabaseVersion(dbCursor)
    
    # get the app_settings from the database...
    appSettingsString = dbGetAppSettings(dbCursor)
    if appSettingsString != "None":
        mergeAppSettings(appSettingsString)

def mergeAppSettings(s):
    global appSettings
    appSettings.update(json.loads(s))
    pass

def saveTasksTable(taskList):
    for task in taskList:
        task.saveToDatabase(dbConn, dbCursor)

def saveAppSettings():
    global appSettings
    appSettingsString = json.dumps(appSettings)
    saved_string = dbSaveAppSettings(dbCursor, appSettingsString)
    if saved_string != appSettingsString:
        error_message_dialog("Application settings not correctly saved... please check...")

def closeDB():
    global dbConn
    dbSaveDatabase(dbConn)

if __name__ == '__main__':
    global dbname
    dbname = cliGetDatabaseName()
    # print(f"Using database file {dbname}")
    ConnectDB(dbname)
    DailyDues()
