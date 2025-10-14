# DailyDues

***A Task Tickler with Time Tracker.***
***(Or is it a Time Tracker with Task Tickler?)***

A helper for managing (and remembering) things that need to be done on a recurring basis, and also tracks the amount of time spent on each. The recurring basis might usually be daily, but it could be weekly, or monthly, or periodically at some other interval.

## Download and Setup
Get the latest version from Github. Open a terminal and navigate to where you want the code to be. 

Then:
```
git clone https://github.com/KobayashiComputing/DailyDues.git
```
Next, go into the newly created 'DailyDues' directory and create a Python virtual environment in which to run the app:
```
cd DailyDues
python -m venv .venv
```
Activate the new virtual environment, then install the required support packages using pip:
```
.\.venv\Scripts\Activate.ps1
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

