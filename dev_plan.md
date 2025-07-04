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

This is more complex than just 'pip install PyGObject'. It looks like we need to use the process described in the [gvsbuild](https://github.com/wingtk/gvsbuild) repository on GitHub.

To run GTK on Windows (without having to build it), download a zip file from the [latest release](https://github.com/wingtk/gvsbuild/releases/tag/2025.6.0) and unzip it to C:\gtk.

It comes with GTK4, Cairo, PyGObject, Pycairo, GtkSourceView5, adwaita-icon-theme, and all of their dependencies.

>Note however that these binaries are provided “AS IS”, WITHOUT WARRANTY OF ANY KIND. They just contain the output of our latest CI run. They are not tested, and we cannot commit to timely updates even for security issues. We strongly recommend to build your own binaries, especially if you plan to distribute them with your application or use them in production.

##### Environmental Variables
Finally, add GTK to your environmental variables with:
```
$env:Path = "C:\gtk\bin;" + $env:Path
$env:LIB = "C:\gtk\lib;" + $env:LIB
$env:INCLUDE = "C:\gtk\include;C:\gtk\include\cairo;C:\gtk\include\glib-2.0;C:\gtk\include\gobject-introspection-1.0;C:\gtk\lib\glib-2.0\include;" + $env:INCLUDE
```

##### PyGObject and PyCairo
If you are going to use PyGObject and Pycairo, you also need to use the gvsbuild generated wheels with your [Python virtualenv](https://docs.python.org/3/tutorial/venv.html) in order to work around this [PyGObject bug](https://gitlab.gnome.org/GNOME/pygobject/-/issues/545):
```
pip install --force-reinstall (Resolve-Path C:\gtk\wheels\PyGObject*.whl)
pip install --force-reinstall (Resolve-Path C:\gtk\wheels\pycairo*.whl)
```

### PyInstaller (for Windows (initially))

A cursory review of the available tools to bundle a Python project into an "executable" indicates that [PyInstaller](https://pyinstaller.org/en/stable/) will likely be the way to go.

