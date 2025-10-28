# Daily Dues
**version 1.0**

By Andy Anderson  
For Boot.dev's first 'Personal Project' as of August 2025  

***A Task Tickler with Time Tracker.***  
***(Or is it a Time Tracker with Task Tickler?)***

A helper for managing (and remembering) things that need to be done on a recurring basis, and also tracks the amount of time spent on each. The recurring basis might usually be daily, but it could be weekly, or monthly, or periodically at some other interval.

## Download and Setup
Open a terminal and navigate to where you want the code to be. 

Then:
```
git clone https://github.com/KobayashiComputing/DailyDues.git
```
Next, go into the newly created 'DailyDues' directory and create a Python virtual environment in which to run the app:
```
cd DailyDues
python -m venv .venv
```
Activate the new virtual environment, then install the required support packages using pip. 

On Windows:
```
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
On Linux:
```
. .venv/bin/activate
pip install -r requirements.txt
```

Finally, run the app:
```
python src\main.py
```

I created a tiny PowerShell script (I named mine 'dd_go.ps1') to activate the virtual environment and run the app:
```
# Note: to run this script you will need to allow unsigned powershell scripts to run on your system, which can 
# be done temporarily by running the following command (as administrator):
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python src\main.py
```

If all goes well, you will see a dialog with notification that the default database file (dailydues.db) was not found, and so one was created. Dismiss the dialog and you should see a new dialog telling you that the database is empty and offering to create some test tasks. 

It's probably a good idea to let it create some test tasks - the default number is 13, but you can choose any (reasonable) number you prefer. If you have more than 11 tasks, the stack of task buttons will be in a scrollable pane inside the main window. Note that you can delete the default database (dailydues.db) and start over from scratch at any time.

## Using the App
### Menu Items
- The 'File' menu currently contains only an 'Exit' option, which exits the application
- The 'View' Menu
    - Choose between the 'Summary' and 'Details' views
    - Indicates which is the 'current' view
- The 'Task' Menu
    - New: Create a new task
        - Displays a new window to enter the options for a new task
        - An error results if you try to change the name to a name that is already used
        - The task is saved to the database and added to the display immediately
        - It's best to use the calendar to pick the date for the next reset, and then modify it manually if needed, keeping the correct format
        - Canceling the window results in no new task being created
    - Edit: Modify user-selectable task properties
        - Displays a new window to edit the options of the selected task
        - An error results if you try to change the name to a name that is already used
        - The task's database entry and the button display are updated immediately
        - It's best to use the calendar to pick the date for the next reset, and then modify it manually if needed, keeping the correct format
        - Canceling the window results in no changes to the selecte task
    - Finish: Mark a task as finished for the current reset period
    - Delete: Completely removes a task from the database
        - NOTE: deletion happens immediately upon confirmation and is not recoverable!
- The 'Help' Menu
    - User Guide: This user manual (eventually)
    - About: Provides information about the app, the database, and some current settings 

### Button Colors
The button colors indicate the state of the associated task. 
- White Text on a Green Background - Ready to start/resume.
- White Text on a Blue Background - Currently working on this task.
- Black Text on a Yellow Background - Danger, needs attention soon.
- White Text on a Red Background - Overdue, it it no longer possible to meet the target for this task during this reset period.
- White Text on a Black Background - Finished, the target for this reset period has been met for this task.
- 'Finished', 'Danger', and 'Overdue' tasks can still be started by clicking them, and the time tracking will be done appropriately.

Note that the 'Exit' button is also White Text on a Red Background!

### Button Actions
Clicking a button:
- Starts/resumes the associated task if the button was *anything other than* White Text on Blue Background
- Pauses the associated task if the button *was* White Text on a Blue Background
- Starting a 'Ready' task will automatically pause any current task. 

### Task Timekeeping
Whenever a task is 'current', the amount of time for the current session, reset period (see below), and total are kept to the nearest tenth of a minute (6 seconds). If the main window is in the 'details' display mode, you can see all of these, along with the target for the reset period and some other info, in the details pane. 

### Daily Usage
Go to the directory where you installed Daily Dues and run the app:
```
python src\main.py
```
It will use the default database unless you supply an alternate path and/or name. To use a different database:
```
python src\main.py <path_to_database>
```
The app should remember where it was located on your screen and start in the same location. It should also remember the 'View' setting and apply that as well. Upon startup, the app will check the next reset date for each task and update it as appropriate, and also adjust the time tracking fields as needed.

#### Overall Approach
The app is intended to help you track the status of tasks that you do every day (or some other recurring period), but not necessarily at the same time each day. The colors of the buttons indicate the current state of each task. 

Each task has a 'reset period', which is how often you want to perform the task. The default reset period is daily, but when you create a new task you can select other options. 

Please note that the timekeeping function is approximate - it should be accurate to within .1 minutes, but is based on when you click the button to start/pause a task. So if you forget to pause a task when you pause working on it, the app will continue to count that time. 

#### How to Start, Pause, and Finish Tasks
Once the app is running, just click on a task button when you are about to start working on that task. Then click the button again to pause the task.

When a task is running, clicking on a different task will automatically pause the current task and upate its time tracking data. 

Once any task's target has been reached, or if you use the 'Task - Finish' menu item to mark a task as finished, that task's button will change to white text on a black background. Note that this is only when the task is not currently 'running' - a task that is currently running will always have white text on a blue background.

Every six seconds (which is .1 minutes), every task is checked to determine if its button should be updated, and the buttons are updated as appropriate. It the app is running at 12:00 a.m., any reset period processing will be reflected in the button (and details, if that view is active) display.

#### Delete Obsolete Tasks from Database
Any task that you no longer need to work on periodically can be deleted. Just use the 'Task - Delete' menu item. NOTE: deletion happens immediately upon confirmation and is not recoverable!
