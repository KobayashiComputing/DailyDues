# Development Plan

This is the overall plan for how to proceed with this project.

## Approach

Overall architecture and design.

### Fundamentals

Task items will be objects of the TaskItem class

TaskItem Objects will have the following state variable, which will have one of the following states at any given time:
- Ready: reset from the previous period and ready to start
- Active: the task item that is currently being done
- Paused: a task item that has been started during this period, is not currently active, and can be resumed
- Finished: a sufficient amount of work has been completed during the current period for the task item to be considered done for the current period

## Frameworks, Tools, and Libraries

### Python

Initial development will be in Python 3.xx, using a virtual environment.

### FreeSimpleGUI

The user interface will be created using FreeSimpleGUI, which is a continuation of the now defunct PySimpleGUI libaray. 

### PyInstaller (for Windows (initially))

A cursory review of the available tools to bundle a Python project into an "executable" indicates that [PyInstaller](https://pyinstaller.org/en/stable/) will likely be the way to go.

