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

#### Port to C/C++

Once I have a solid minimum viable product (MVP), I will probably attempt a port to C/C++. This will be both an exercise to rebuild my C language skills and a comparison of the different development approaches.

### SQLite (Database)

This will be the starting database at least, and my serve for future versions as well.

### Graphical User Interface

I'll use a free, (most likely) open-source GUI toolkit. Theoretically, one that supports multiple languages and is available on both Windows and Linux would be preferable.

#### FreeSimpleGUI

On option for the user interface is [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGui), which is a continuation of the now defunct PySimpleGUI libaray. Downside is that it only supports Python (I think). 

[Documentation](https://freesimplegui.readthedocs.io/en/latest/) for FreeSimpleGUI.

#### (or maybe) GTK

An option for the UI is [GTK](https://www.gtk.org/). This one is mature, with support for both Python and C/C++, and is available for both Windows and Linux.

#### GUI Toolkit Integration

Whichever GUI toolkit is ultimately used, it will need to be isolated so that the it can be updated separately from the main project.

### PyInstaller (for Windows (initially))

A cursory review of the available tools to bundle a Python project into an "executable" indicates that [PyInstaller](https://pyinstaller.org/en/stable/) will likely be the way to go.

