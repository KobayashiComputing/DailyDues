import re
from datetime import datetime
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

def validate_datetime_format(date_string):
    """
    Validates if the given string matches the format 'YYYY-MM-DD HH:MM:SS'.
    Returns True if valid, False otherwise.
    """
    # Define the regex pattern for 'YYYY-MM-DD HH:MM:SS'
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\s(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
    
    # Check if the string matches the pattern
    if not re.match(pattern, date_string):
        return False

    # Additional validation using datetime.strptime
    try:
        datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return False

    return True
