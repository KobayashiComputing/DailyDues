import FreeSimpleGUI as sg

def app_user_guide():
    # All the stuff inside the window.
    layout = [
        [sg.Text('Daily Dues (or "Daily Do\'s") User Guide')],
        [sg.Text(f'Canonical info at https://github.com/KobayashiComputing/DailyDues')],
        [sg.Text(f'')],
        [sg.Text(f'(This will be filled in real soon now... ;-) )')],
        [sg.Text(f'')],
        [sg.Push(), sg.Ok()]
    ]

    # Create and show the Window
    tempWindow = sg.Window('Task', layout, modal=True)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = tempWindow.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    tempWindow.close()
    return True

def app_about(dbName = "unknown", appVersion="0.00", dbVersion="0.10", sgKeyNdx=0, bg_counter=0):
    # All the stuff inside the window.
    layout = [
        [sg.Text('Daily Dues (or "Daily Do\'s")')],
        [sg.Text('A task tickler with time tracking...')],
        [sg.Text('(or a time tracker with task prioritization)')],
        [sg.Text('     ')],
        [sg.Text(f'By Andy Anderson, for Boot.dev\'s First Personal Project')],
        [sg.Text(f'')],
        [sg.Text(f'More info at https://github.com/KobayashiComputing/DailyDues')],
        [sg.Text(f'')],
        [sg.Text(f'The following might be useful for debugging:')],
        [sg.Push(), sg.Text(f'Database Connected: {dbName}')],
        [sg.Push(), sg.Text(f'App Version: {appVersion}')],
        [sg.Push(), sg.Text(f'Database Version: {dbVersion}')],
        [sg.Push(), sg.Text(f'Current Housekeeping Cycle: {bg_counter}')],
        [sg.Push(), sg.Text(f'Main Window Distinguisher Key: {sgKeyNdx}')],
        [sg.Text(f'')],
        [sg.Push(), sg.Ok()]
    ]

    # Create and show the Window
    tempWindow = sg.Window('Task', layout, modal=True)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = tempWindow.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            break

    tempWindow.close()
    return True
