# Requirments for DailyDues

## Nomenclature and Definitions

1. Task Item: a self-defining process that the user wants to do every reset period
2. Reset Period: how often a task item that has been "Finished" automcatically changes back to "Ready"
3. User: the individual who is using this software
4. Task Item State: any one of the following
    - Ready: can be started at any time, but has not been started during the current reset period
    - Current: active at the present time (only one task item can be current at any time)
    - Paused: has been started during the current reset period, but another task item is current at the present time
    - Finihsed: the task item has been completed for this reset period


## Functional Requirements

- I can add, sort, archive, and delete task items
- I can Start, Pause, Resume, and Check Off task items
- Task Items reset their "Checked Off" state at the appropriate interval
- I can toggle between available task items
    - Toggling any Task Item to "on" or "currently working" or whatever 
    pauses any other "active" task item
    - "Checking off" or "finishing" a tast item for the day does not 
    automatically resume any other task item
- I get helpful text balloons for all buttons in the interface
- I can show or hide detailed info about the current active task item
- I can have the list of task items automatically sort by which one "should"
be next
- I can choose the time of day that my finished tasks reset
- I can hide or show task items that have been finished for the day
- I can set task items to be every day, only weekdays, only weekend days, 
select specific days
- I can group task items
