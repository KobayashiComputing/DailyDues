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

### Requirements and Definitions

The initial, informal requirements list (in the form of "I can..." statements), as well as nomenclature and definitions for this project, can be found in the [requirements.md](requirements.md) file.

### Minimum Viable Product (MVP)

The initial, or startup, Minimum Viable Product (MVP) will be:
1. Developed in Python 3.1x using FreeSimpleGUI in a virtual environment.
2. Run on Windows 11
3. Address the following requirements:
    - I can ADD a Task Item
    - I can EDIT a Task Item
    - I can SORT Task Items
    - I can ARCHIVE a Task Item
    - I can DELETE a Task Item
    - I can Start a Task
    - I can Pause a Task
    - I can Resums a Task
    - I can Check Off (finish for the current period) a Task
    - Task Items reset their "Checked Off" state at the appropriate interval
    - I can toggle between available task items
        - Toggling any Task Item to "on" or "currently working" or whatever pauses any other "active" task item
        - "Checking off" or "finishing" a task item for the day does not automatically resume any other task item   



## Frameworks, Tools, and Libraries

### Python

Initial development will be in Python 3.xx, using FreeSimpleGUI, in a virtual environment.

#### Port to C/C++

Once I have a solid minimum viable product (MVP), I will probably attempt a port to C/C++. This will be both an exercise to rebuild my C language skills and a comparison of the different development approaches.

One decision that will need to be made at that time (if not before) is which C/C++/C# toolchain to use.
- MSYS2
- MSVC

### SQLite (Database)

This will be the starting database at least, and my serve for future versions as well.

### Graphical User Interface

I'll use a free, (most likely) open-source GUI toolkit. Theoretically, one that supports multiple languages and is available on both Windows and Linux would be preferable.

#### FreeSimpleGUI

On option for the user interface is [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGui), which is a continuation of the now defunct PySimpleGUI libaray. Downside is that it only supports Python (I think). 

[Documentation](https://freesimplegui.readthedocs.io/en/latest/) for FreeSimpleGUI.

##### PyGObject and PyCairo
If you are going to use PyGObject and Pycairo, you also need to use the gvsbuild generated wheels with your [Python virtualenv](https://docs.python.org/3/tutorial/venv.html) in order to work around this [PyGObject bug](https://gitlab.gnome.org/GNOME/pygobject/-/issues/545):
```
pip install --force-reinstall (Resolve-Path C:\gtk\wheels\PyGObject*.whl)
pip install --force-reinstall (Resolve-Path C:\gtk\wheels\pycairo*.whl)
```

### PyInstaller (for Windows (initially))

A cursory review of the available tools to bundle a Python project into an "executable" indicates that [PyInstaller](https://pyinstaller.org/en/stable/) will likely be the way to go.

