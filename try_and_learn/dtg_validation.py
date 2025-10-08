"""
I got this file from Bing.com's 'Copilot Search' AI agent... I searched for
the following string:

    python use regex to check format of datetime string

I'm going to use the function as-is by adding it to my 'helpers.py' file...

"""

import re
from datetime import datetime

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

# Example usage
test_dates = [
    "2023-10-08 14:30:45",  # Valid
    "2023-02-30 14:30:45",  # Invalid (Feb 30 doesn't exist)
    "2023-10-08 25:30:45",  # Invalid (Hour > 23)
    "2023-10-08",           # Invalid (Missing time)
    "2023-10-08 14:30"      # Invalid (Missing seconds)
]

for date in test_dates:
    print(f"'{date}' is valid: {validate_datetime_format(date)}")
