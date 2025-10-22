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
