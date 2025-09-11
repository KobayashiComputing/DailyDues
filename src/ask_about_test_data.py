import FreeSimpleGUI as sg
from task import *

def askAboutTestData(db):
    # sg.theme('Dark')   # theme for this window, or all of sg?

    # The layout for the FreeSimpleGUI window.
    layout = [
        [sg.Text(f'The database ({db}) is empty, possibly newly created.')],
        [sg.Text('Do you want to populate it with test data?'), sg.InputText(default_text='13', key='test_count')],
        [sg.Yes(), sg.No()]
    ]

    # createTestData will be our return value, defaulting to 'False'
    createTestData = False
    testDataCount = 0

    # Create and show the Window
    form_new_task = sg.Window('Create Test Data?', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = form_new_task.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break

        if event == "Yes":
            createTestData = True
            testDataCount = int(values['test_count'])
            break

        if event == "No":
            createTestData = False
            testDataCount = 0
            break
        
    form_new_task.close()
    return createTestData, testDataCount

