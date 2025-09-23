from form_really_do_it import *
from form_error_message import *
from task import *

def reallyDoIt(msgString):
    return really_do_it(msgString)

def isDuplicateTask(taskName, taskList):
    if next((i for i, t in enumerate(taskList) if t.name == taskName), -1) != -1:
        return True
    return False

def displayErrorDialog(msgString):
    return error_message_dialog(msgString)