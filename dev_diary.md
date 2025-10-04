# Development Diary

## 2025-07-13 (Sunday)
I'm a little late starting this. Some of what should have been in a file like this is actually (erroneously) in the dev_plan.md file.

I really try not to work (too much) on Sunday...

FreeSimpleGUI has worked well so far. I had a *little* trouble getting the correct stuff 'pip install(ed)' but I got it worked out.

GTK (and GTKMM) has been a frustrating mess. I've already spent **way** too much time and effort on trying to get the 'hello_world_gtk.cpp' to even compile, and I've now officially given up on GTK. I had the MSYS2 environment installed already with both the MinGW and UCRT implementations of gcc and g++ set up. After most of a week trying to get the correct incantations to make it work with VS Code, I at least got it to work from within the MSYS2 MINGW64 shell. That is, I could compile my hello world tests from the command line within that environment and get working executables, but I just never could get it to work from within VS Code. I finally got all of the include directories in the tasks.json build task, but then the linker/loader could not find the symbols in any of the many libraries I added to the g++ args. 

So today I'm looking into what other cross platform C/C++ compatible GUI toolkits are available that will work with VS Code. I'm hoping to find one that is compatible with/compilable by MSYS2 UCRT (Universal C Run Time) tool chain. 

Here are the current contenders:
- [Qt](https://www.qt.io/) is a possibility, although I've heard bad things about their business practices and licensing
- [wxWidgets](https://wxwidgets.org/) looks really promising (that's the next one I'm going to try... I think...)
- [Xtd](https://github.com/gammasoft71/xtd)
- [Elements](https://github.com/cycfi/elements) is a strong contender
- [MyGUI](https://github.com/MyGUI/mygui) might be worth a look

Note: [Sciter-JS](https://gitlab.com/sciter-engine/sciter-js-sdk) looks interesting for HTML/CSS/JavaScript development of desktop apps. (For future reference.)

Note 2: [Noesis Engine](https://www.noesisengine.com/noesisgui/) looks promising for game development.

**Task 1 for Today:** reinstall MSYS2 compiler(s) and dev tools for use with VS Code, accoring to the official [setup guide](https://code.visualstudio.com/docs/cpp/config-mingw) on the Visual Studio Code site. I also followed the rest of the steps on the site to create the 'helloworld.cpp' test code, as well as the tasks.json, launch.json, and c_cpp_properties.json files.

This wasn't as easy as it should have been. Somehow, VS Code (or, more likely, the C/C++ Extension) was still looking for the g++ compiler at 'c:/msys2/mingw64.bin/g++.exe' even though I had deleted the original *.json files. I created a new 'settings.json' and entered the new compiler path (for the UCRT tool chain) and I also closed the folder and VS Code, and then started them up again, and somehwere in there it finally got the new configuration (at least for now). Maybe this [doc](https://code.visualstudio.com/docs/languages/cpp) for the C/C++ extension will be helpful.

The [Variables Reference](https://code.visualstudio.com/docs/reference/variables-reference) will likely be useful. Actually, it already had been:

>You can reference environment variables with the ${env:Name} syntax. For example, ${env:USERNAME} references the USERNAME environment variable.

```
{
  "type": "node",
  "request": "launch",
  "name": "Launch Program",
  "program": "${workspaceFolder}/app.js",
  "cwd": "${workspaceFolder}",
  "args": ["${env:USERNAME}"]
}
```

## 2025-07-14: (Monday)
I got wxWidgets installed and the 'wxwin' environment variable set. Copied the sample 'helloworld.cpp' code to a file and attempted to compile and debug. I did get the intellisense stuff working, but the compiler could not find some (many? most?) of the include files, so no joy. 

I'm now considering trying to get the right configuration in VS Code to develop with the official WinUI libraries, but it seems like Microsoft only wants Visual Studio used for 'actual Windows' development. sigh.

## 2025-07-15: (Tuesday)
No real substantive work on this project today. Still reading some of the Microsoft websites and docs regarding WinUI and other dev frameworks for Windows desktop applications. I found [this reference](https://learn.microsoft.com/en-us/windows/apps/get-started/?tabs=uwp%2Cnet-maui&WT.mc_id=dotnet-35129-website) today, and that looks like the next thing to read (and I'm hoping it will shed some light on which path to take).

This [page](https://learn.microsoft.com/en-us/training/modules/winui-101/) should be helpful ("WinUI 101").

I'm going to work thru [this](https://learn.microsoft.com/en-us/windows/apps/get-started/start-here?tabs=vs-2022-17-10&source=docs) in the near future; it will be in a different "Project" with a different GitHub repo.

Also, I notice that Microsoft Ignite is going to be held Nov 17 thru 21 this year (2025). I signed up for (and will actually pay attention this year).

## 2025-07-19: (Saturday)
As much as I'd like to use VS Code for all of my editing, it is looking very much like I'll need to learn Visual Studio if I want to do any C++ with a GUI for Windows. Sigh. 

## 2025-07-21: (Monday)
Minor additions to 'dev_plan.md."

## 2025-07-22: (Tuesday)
I took another look at wxWidgets - the documentation isn't as approachable as it could be or I'm a lot more dense than I could be, but at any rate I was able to make some progress with it. However, it is apparent that learning how to use wxWidgets is going to be a project in its own rite, so I'm going to move that effort to another project with its own repo.

I hope to work on both in parallel... we'll see...

## 2025-07-23: (Wednesday)
Created another project and repo - wxWidgets_My_Way - and copied the mxWidgets sample code, and all of the C/C++ code to it. 

## 2025-07-24: (Thursday)
Removed all of the "other" GUI framework directories and code from this project, so this project will be pure Python and FreeSimpleGUI for the foreseeable future. Also removed the *.json files from the .vscode directory. 

## 2025-07-28: (Monday)
Copied the "How to Spell Do's and Don'ts.pdf" into this project.

## 2025-08-23: (Saturday)
I finished the Boot.dev course titled "Memory Management in C" today, and the next course is the "First Peronsal Project," which is *this* project! I should be starting this in earnest on Monday (August 25, 2025).

One other minor update for today: I changed the name of the "requirements.md" file to "dev_requirements.md" to avoid any confusion with the "requirements.txt" file (which is used by/for pip).

## 2025-08-24: (Sunday) (Start of Actual Coding)
Moved source code from 'floating_toolbar_2.py' to 'main.py' and moved 'main.py' to the main 'src' directory. The code from the floating toolbar 2 example becomes the base for this project. 

## 2025-08-25: (Monday)
Searched the web for "Preferred structure for Python applications" and found the following:
- Layouts from [RealPython.com](https://realpython.com/python-application-layouts/)
- Modules and Packages intro from [RealPython.com](https://realpython.com/python-modules-packages/)
- How-To from [PowerfulPython.com](https://powerfulpython.com/blog/how-to-write-larger-more-complex-applications/)

Based on the 'Layouts' post, I plan to use the layout for 'Applications with Internal Modules,' which may be overkill for this app, but should be good practice for building a good habit.

Modified directory structure and layout and added 'bin', 'docs', and 'tests' directories i preparation for ramping up development. Renamed 'test_and_learn' directory to 'try_and_learn' to avoid confusion with 'tests' directory.

I need to delve into the 'Python Modules and Packages' article on [RealPython.com](https://realpython.com/python-modules-packages/).

## 2025-08-26: (Tuesday)
Removed superfluous original example code, created 'task.py' file to contain task object and related code, and created a rudimentary task object definition. Added class variable for 'current_task' and methods to get and set it.

## 2025-08-27: (Wednesday)
Reworked some instance var names for the Task class. Removed superfluous code from the main while loop. Worked on logic to start/switch tasks.

## 2025-08-28: (Thursday)
Got task state change from UI working, including cleaning up 'current' task before exiting.

To-Do: determine color scheme for various states. Maybe this:
  - Green: Ready to Start, whether paused or not yet started this period
  - Blue: Running/Current
  - Black: Finished for this period
  - Yellow: Within X amount of time until 'overdue' (end of period without target time spent)
  - Red: Overdue

Also, it would be great to have the play/pause/stop/eject symbols for the 'buttons'

To-Do: determine what text/icons show up on the 'Task Buttons'

Hmmm... updating the window is not working the way I thought it would, so need to look closely at [this page](https://freesimplegui.readthedocs.io/en/latest/#pattern-2-b-persistent-window-multiple-reads-using-an-event-loop-updates-data-in-window) in the docs.

## 2025-08-29: (Friday)
After reading the documentation (what a concept!), I was able to update the 'button_color' setting for the buttons for specific tasks. The state changes from 'ready' to 'current' to 'paused' and for switching to a new task are all working. 

I think the next step will be to connect with a database (using SQLite at least for the beginning). This will allow me to save the task info, so I can then start keeping track of time spent on each task. 

Got command line arguments handling done (using 'argparse'), and got and SQLite3 database connected.

## 2025-08-30: (Saturday)
Investigating ways to convert task objects into something(s) that can be stored in the database. 

Using the .__dict__ attribute for the object works to create a dictionary, then getting a string representation of that dictionary to store and then ultimately convert back to a dictionary which could be used to recreate the object looked promising. However, I guess the ENUMs I'm using trip up both the JSON and EVAL (the straight 'EVAL' and the ast.literal_eval) methods/functions when trying to convert the string back into a 'real' dictionary. 

SQLAlchemy was mentioned in ths [StackOverflow](https://stackoverflow.com/questions/2047814/is-it-possible-to-store-python-class-objects-in-sqlite) article, and that may be the 'best' way to go. 

A Wikipedia article on [Object-Relational Mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)...

I *might* do it manually with a class method that returns a databaseable string or strings or whatever and then another method that turns that string back into an object... just to get the experience... we'll see.

## 2025-08-31: (Sunday)
Before charging ahead with designing the database and creating queries, it occurs to me that we need to know whether or not the database existed before we opened it, or if it was newly created. Maybe the easiest way to know would be to check for the file first, or maybe get a list of tables after the open/create operation? I'm going to use the 'get a list of tables' approach...

This [article](https://codefather.tech/blog/sqlite-database-python/) from codefather.tech looks helpful.

### Code to get a list of tables from sqlite3:
```
SELECT name 
FROM sqlite_schema 
WHERE type = 'table' 
ORDER BY name;

```

## 2025-09-01: (Monday)
Working on database design and inialization today and likely for the next couple (or few) days. Along with that, this may be a good time to start working on the FreeSimpleGUI form to create/edit a task, as that's some of the data that will go into the database. 

Actually, I've gotten the code to create the 'tasks' table working, although it will almost certainly need some updates as I go along.

I've decided to write the code to save the taskList to the database next. Initially, it will save, and them maybe 'update' the bogus taskList that I've been used for development. Then I'll - hopefully - use that code as a model to read the taskList from the database at startup. I've got the flow in the code for the basic approach already: 
- catch EXIT or window close 
- clean up the state of Task
- call 'saveTasksTable()
  - loop through the taskList 
    - call 'task.saveToDatabase' for each task
      - convert the task object into savable strings/integers
      - call 'dbUpdate(cursor, tableName, valuesDictionary)' to insert or update the record as appropriate
- close the database
- close the window (thus ending the process)

This flow is now working down to and including checking the existence of the selected record. Next step is to actually write the record data into the database. 

The code to write the records to the database is written and working, and that's enough for today. Tomorrow I'll work on reading the data back from the database and using it to initialize the 'taskList'.

Note: TO-DO - the main window with the stack of task buttons needs to be resizable, specifically to make it shorter with a scrollable stack of buttons. It would be nice for the 'Exit' button to always show at the bottom of the stack.

## 2025-09-02: (Tuesday)
Side task excursion for today: make the stack of buttons resizable on the 'Y' axis with a scrollbar. It looks like this will require a slightly different layout. I'll need a layout with a column element for the button stack with a button below for the 'Exit'.

That was actually pretty simple. See the code for the changes that were needed ;-)  

This also solved the issue of the 'Exit' button fixed at the bottom. And... adding a menu row at the top should be easier now.

Hmmm... testing a task list with more than 10 tasks (0 - 9) exposed a problem: I was checking for the current task with a 'task.name in event' construct, but it needed to be 'task.name == event'. That's fixed now.

Testing with various numbers of tasks in the task list to see how that changed the window size. Apparently the default size of the window (vertically) is something like 60% of the height needed to show all 'rows' in the layout. 

Added code flow to get the list of tasks from the database. Now I just need to fill in the function bodies.

## 2025-09-03: (Wednesday)
Added code to get the task records out of the database and create a dictionary for each record that includes the field name and the data (so this will all still work if any fields are inserted at a later date - hopefully). Then wrote a function in the Task object to create a task object from a dictionary (slyly named it 'newTaskFromDictionary()'). Everything is working except I need to write convertor functions to handle converting the datetime and deltatime objects to and from strings to store in the database. 

Read from database working, but need to sanitize the text fields in case they have any quote marks in them. 

ToDo: think about if session start, stop, and paused DTG should be propagated as "None."

## 2025-09-04: (Thursday)
The mechanics are working so far. Need to think about the question above from yesterday, as well as start really thinking about:
- new task creation form
- task editing form
- re-sorting buttons in the stack on *significant* state changes (that is, 'finish', 'hit target')
- how the 'reset' is going to work and where it will be implemented (these are obviously related)

Also, need to change the state to 'READY' when saving to the database when shutting down... (I just took care of this).

## 2025-09-05: (Friday)
Added a menu bar with what I think will be the actual, final menu items. Next effort will be in the 'New' and 'Edit' items on the 'Task' menu. This will require an additional, separate window.

Added a 'match - case' block with cases for each of the menu items.

## 2025-09-06: (Saturday)
No real code changes today... planning to look at how to create a FreeSimpleGUI window with a form to create a new task or edit an existing task. Not sure how easy (or difficult) that's going to be. Yet. ;-)

## 2025-09-07: (Sunday)
I will be changing the Task class so that the 'reset' field is the DTG of the *next* reset time, instead of the duration until the next reset. Then, I'll need to implement a timer to run a function to check the reset time of all tasks to see if it has passed, and, if so, 'reset' that task's state and status. This will be a major change, and might require deleting and recreating all of the current databases... or maybe not.

## 2025-09-08: (Monday)
Updated the 'reset' field in the Task class as outlined above. I changed the data in the current database file with 'DB Browser for SQLite' and it worked like a charm.

## 2025-09-09: (Tuesday)
Progress on the form for adding a new task.

## 2025-09-10: (Wednesday)
More progress on the 'new task' form.

## 2025-09-11: (Thursday)
Added logic to check for empty database and ask if the user wants to add 'test' data. This will be useful while in development, but will be removed for production use. 

## 2025-09-12: (Friday)
Some minor changes to documentation and some comments. Some testing and debugging as well.

## 2025-09-13: (Saturday)
More work (and some experimentation) on the form to create a new task.

The form it *mostly* finished and working. Still need to
- check if the new task name is already used and act appropriately
- create a function to calculate the reset date given the created date and frequency...

Once the new task functionality is completely working and added to the 'taskList', then I'll need to update the main window (and I don't know how to do that... yet...).

That's enough for today... probably...

From something Bing search found on the Internet with Copilot:
```
The sqlite_schema table, previously known as sqlite_master, has been a 
core part of SQLite since its early versions. It serves as a system table 
that stores metadata about the database schema, including tables, indexes, 
triggers, and views. The name sqlite_schema was introduced in SQLite 
version 3.33.0, released in August 2020, to align with its purpose more 
clearly.

```

## 2025-09-14: (Sunday)
Added the 'taskList.append(newTask)' line to the conditional after calling 'newTaskForm()' and returning a new task object. This works (wasn't too worried about that), but, of course, it does not show up in the button stack in the main window unless the application is closed and then restarted. The fact that it shows up when closed and restarted implies that it's getting stored into the database correctly. I looked a the database with sqlitebrowser and, yes, it is in fact being stored in the database, and it's *almost* correct. The 'reset' in the database shows up as '1' instead of the enum 'ResetFrequency.DAILY', so I need to fix that. 

Added a couple of lines of code to convert the frequency chosen from the list into a value for the ResetFrequency enum, and then into the proper string (as it appears in the database), and then replaced the value in the 'values' dictionary. To wit:
```
  fNdx = freqList.index(values['frequency'][0]) + 1
  eName = next((member.name for member in ResetFrequency if member.value == fNdx), 'DAILY')
  values['frequency'] = f"ResetFrequency.{eName}"
```
Yes, I could combine all of that into a single line of code, but that line would be *long* and somewhat less clear (I think).

Thinking about how to 'replace' the button stack, which is in a column element in the main window, I'm hoping it will be possible to simply add the button for the new task (which is already added to the 'taskList') and then use the update() method on the column element something like the code below:

```
  taskList.append(newTask)
  buttonStack.append([
          sg.Button(f'{newTask.name} (P:{newTask.priority})', 
          button_color=Task.task_color_pairs[newTask.state.value],
          key=newTask.name)
      ])
  window["ButtonColumn"].update(buttonStack)
  window.refresh()
```

After some review of the FreeSimpleGUI documents, and a couple of questions on StackOverflow and Reddit asking about exactly this situation, the appears to not be possible. The accepted approach is evidently to create a new window of the same size (or presumably larger, as necessary) in the same location (the x,y coordinate of the upper left window corner) and then to close the old window. 

Sigh. Trying to use the same function to create a new window produces an error that the layout for the column had already been used, and that a 'new, fresh layout' (or something to that effect) has to be used each time. The problem seems to stem from duplicate 'key' values for the task buttons. Maybe using an additional identifier appended to the key will work? I could swap back and forth between 'w0' and 'w1' to identify which window the task buttons will be in...

That will likely require putting the code to create the button stack into the 'show_button_stack()' function and passing in the taskList and a 'main' window identifier. That would somewhat simplify adding the button for the new task to the buttonStack, as it would just be done in the 'show_button_stack()' function. It sure would be a lot easier if FreeSimpleGUI had an update function that could replace the layout of an element with a new/modified layout.

## 2025-09-15: (Monday)
Yesterday's efforts spilled into the early morning of today. 

## 2025-09-16: (Tuesday)
Vacation day!

## 2025-09-17: (Wednesday)
Vacation day!

## 2025-09-18: (Thursday)
Vacation day!

## 2025-09-19: (Friday)
Travel day.

## 2025-09-20: (Saturday)
Back in the 'office' today. So... where was I... oh, yeah, trying to *refresh* the stack of task buttons in the main window when the task list is updated. I'm going to try to create a new window with the updated task list, then close the original window, then reassign the new window's handle to the original variable. We'll see...

That doesn't quite work, but I think I'm getting closer. The 'layout' for the column element generates a FreeSimpleGUI error that - if I'm understanding it correctly - is complaining about the keys used for the buttons. I think what it means is that I need new, unique, keys for the buttons. I will try to generate 'new' keys by appending a string version of a counter to each one. In order to do this, it will be better to pass the taskList into the 'show_button_stack()' function and build the buttonStask there...

Hmmm... so the 'event' that is returned when a button is pressed is the *key* for that button. Moving the buttonStack creation loop into the 'show_button_stack()' function, with a pseudo-window-identifier (as in code below) solved the problem.
```
    global sgKeyNdx, sgKeyList

        ...
    
    # increment the sgKeyNdx... do this here so that the global value is the same throughout this file
    sgKeyNdx = (sgKeyNdx + 1) %5
    
    # build the buttonStack with the sgKeyList[snKeyNdx] string appended to the key values of the buttons...
    buttonStack = []
    for task in taskList:
        buttonStack.append([sg.Button(f'{task.name} (P:{task.priority})', 
                                      button_color=Task.task_color_pairs[task.state.value], 
                                      key=task.name+sgKeyList[sgKeyNdx])])
```

Okay! That works! Now I need to get the new window to appear at the same place as the old window. Getting the old windows location was easy (window.current_location()) and passing that into the 'show_button_stack()' function as a named paramater - and then actually using that in the window creation - did the trick.

## 2025-09-21: (Sunday)
Next thing to do is the 'Task Delete' menu item. Hopefully this will be easier now that I have the 'show_button_stack()' function handling the creation of a new, updated window. The trick here will be to determine which task to delete. I think my approach will be to add another dropdown list to the 'Task | Delete' menu item. This *should* be as simple as creating a list of possibly abbriviated task names and passing it in as an additional parameter into the 'Menu'.

This is working to display the current list of tasks as a submenu from each of the menu buttons ('Edit' and 'Delete'). The way to distinguish *which* button it is - and differentiate either from the task buttons in the main stack - is by using menu keys. So in the loop to create the task buttons for the main button stack, I just added the following to create the lists for edit and delete.
```
        deleteTaskList.append(f'{task.name}::Delete')
        editTaskList.append(f'{task.name}::Edit')
```

That works, and adding the following code just before the 'match-case' statement for the menu handling gets us to the point in the code where we need to be for each case:
```
            # The 'Task' menu has two submenus - 'Edit' and 'Delete', and we need to determine if our event
            # is one of those...
            tmpNdx = event.find('::')
            if tmpNdx != -1:    # we have an edit, a delete, or a problem...
                tmpTaskID = event[:tmpNdx]
                event = event[tmpNdx+2:]
```

I need to remember this code for finding the index of an object in a list of objects:
```
  index = next((i for i, obj in enumerate(my_list) if obj.<attribute_name> == <value_sought>), -1)
```

Finally (for today), created a function 'update_main_window()' to call whenever the tasklist changes. It creates a new window over the old one, paints it, and then closes the old window.

## 2025-09-22: (Monday)
Finished the 'Task - Delete' functionality, which included some updates to a couple of other functions. The 'New Task' and 'Delete Task' functionality is now completely working.

Got the 'Task - Edit' functionality working. I need to go back and add input checking to both the 'New Task' and 'Edit Task' functions, and check to make sure that the name is not only provided, but is also unique.

Added checks for empty fields for 'New Task' and 'Edit Task', and check for duplicate name for 'New Task', but still need to display error message in a modal window...

## 2025-09-23: (Tuesday)
'New Task' and 'Edit Task' functionality working with error display in modal window.

Grayed out menu items that have not yet been implemented.

Added 'Housekeeping' hook to main loop, but not doing any just yet (just printing a line when it runs).

Some progress calculating reset datetime. I think I've got the creatition time correct. These are in both the 'Task - New' and 'Task - Edit' functions. 

## 2025-09-24: (Wednesday)
Added call to 'displayErrorDialog()' for duplicate task name for both 'Task - New' and 'Task - Edit'.

Added logic to handle session duration and total duration. 

Still need to work on:
- 'Finishing' a task for the current period
- Sorting of the button stack according to task priority, etc.
- Updating button colors when tasks get close to their reset without new work
- Updating button colors when tasks are overdue

## 2025-09-25: (Thursday)
After working on the timekeeping functionality, it occurs to me that I will need to add a field to the Task object (and, subsequently, to the database) to keep track of 'duration this period'. I will work on that today.

Added the field for 'duration_period' (the amount of time spent on a task during the current reset period), to the Task object and the database. Also added code to update it when the task it started or paused. Note that determinining when a task is 'finished' will be done whever it is paused, and if it is finished, the state will be set accordingly. Also, note that even a 'finished' task can be started again during the same reset period.

## 2025-09-26: (Friday)
With much of the coding done, it's time to think about where I am in this project, what's left to do, and what to do next. 

Everything works for adding, modifying, updating, and deleting tasks. Tracking time spent on an active task is working as well. The app is, I think, in a usable state - for me, but not for anyone else at this point. 

So, what's left? 
- The 'details' display window (the 'View' menu items).
- Sorting and re-sorting the list of task objects as tasks get 'finished' and other tasks get near a state of 'overdue.'
- Reset period processing, which will impact the sorting/re-sorting as well as the colors of the buttons through the reset period.
- 'Housekeeping' function(s), which will handle both of the above, and probably more as well.
- Implement the remaining menu items (some of which might just be removed).
- Checking the version of the database on startup and update the database as needed.
- Unit tests for all (most? some?) of the functions.
- The 'D' word - *documentation* (gasp!).

Activity for today: I changed the dbVersion string from "0.00a" to "0.10" (and updated this file!).

I also created the functions for the 'Help' menu, and either commented out all 'print()' statements, or changed them to calls to 'error_message_dialog()'.

Added base code to support 'Details' view vs 'Summary' view. Now I need to fill in the details in 'Details' view...

## 2025-09-27: (Saturday)
It occurs to me that I could/should store a couple of additional pieces of data in the database:
- The last location of the main window when it's closed
- The state of the 'View' when the main window was closed (or maybe when the 'View' is changed?)

Thinking about how to keep these data items together and 'at hand', I wonder if a dictionary would be appropriate, and maybe that would be the easiest thing to store in the database? Adding and updating items in the dictionary would be easy, and if it could be converted to a long string and stored in the database that way, that would reduce the number of changes to the database schema (and, also, the code), although I'd need some mechanism to get new items into the dictionary between reading from and writing to the database. This problem might be overcome by:
- Creating and initializing the dictionary early in the code
- Read the string from the database
- Convert the string to a second, temporary dictionary
- 'Update()' the first dictionary (from the code) with the items from the second dictionary
- use the dictionary in the code
- Convert updated dictionary to string and store in db at shutdown

The following code works to do just that:
```
    import json

    # Set up the dictionaries
    settings_from_code = {"name": None, "age": None, "city": None, "lastname": None}

    settings_from_db = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    string_from_db = json.dumps(settings_from_db)
    settings_from_db = json.loads(string_from_db)

    # use the 'update()' method to update one dictionary with items from the other
    settings_from_code.update(settings_from_db)

    # now we can use 'settings_from_code' in the code with the appropriate values 
    # from the database, and new items with the default values
    print(settings_from_code)
```

Created an 'appSettings' dictionary to contain various settings related to the app, and will store this in the database soon.

## 2025-09-28: (Sunday)
Taking today off (mostly...)

## 2025-09-29: (Monday)
Updated database schema to include a field for the 'appSettings' string version.

Added code to save and get the 'appSettings' to and from the database, and appropriately merge them with the existing settings from the code. Also added a 'dbGetDatabaseVersion()' function to get the database version when the database is not empty at startup. 

## 2025-09-30: (Tuesday)
Added code to show a FreeSimpleGUI 'multiline' element with the details of the tasks in the task button stack. Next, I'm going to create a function to return the string used for the details pane, because it will need to be updated during the housekeeping and possibly other times as well.

Added method 'getTaskDetailsString(self)' to 'task.py', and it works well.

So, the details pane - for only the current, active task - should be updated during 'housekeeping' *if* the details pane is being displayed. Other times it might make sense to update it (again, if the details pane is displayed):
- when a task is started
- when a task it paused/stopped
- when another task is started

Corrected an error in the way I was computing durations for the current reset period and the total. I *think* it's fixed now.

## 2025-10-01: (Wednesday)
Changed the 'timeout' on the 'sg.window()' call to 6 seconds (which is .1 minutes), and changed the display to round to the nearest tenth of a minute. 

Everything so far seems to be working, and I've started using the app on my local machine. 

So, ***now*** what's left? To my mind (in the order I'll probably do them):
- Reset period processing, which will impact the sorting/re-sorting as well as the colors of the buttons through the reset period.
- Sorting and re-sorting the list of task objects as tasks get 'finished' and other tasks get near a state of 'overdue.'
- 'Housekeeping' function(s), which will handle both of the above, and probably more as well.
- Implement the remaining menu items (some of which might just be removed).
- Unit tests for all (most? some?) of the functions.
- The 'D' word - *documentation* (gasp!).
- Checking the version of the database on startup and update the database as needed.

I plan to 'release' the first version once the reset period processing and sorting/resorting is complete and added to 'housekeeping'. That will still leave a lot of typing to do.

I've already started thinking about how to do the reset period processing, but it's all vague at this point. I will likely try out some approaches in the 'try_and_learn' directory. 

## 2025-10-02: (Thursday)
Thoughs on the algorithm to use for reset period processing:
- The next reset date should be a multiple of the reset period added to the last know reset date
  - multiplier = int(days_since_last_reset_date / reset_freq_days)
  - next_reset_date = last_reset_date + (delta_days * multiplier)
- This should only happen if the last reset date has passed (or is today?)

Maybe something like this:
```
    # the number of days in each of the ResetFrequencies
    day_counts = {
        "DAILY": 1,
        "WEEKDAY": 5,
        "WEEKLY": 7, 
        "WORKWEEKLY": 5, 
        "BIWEEKLY": 14,
        "MONTHLY": 30,
        "QUARTERLY": 91.313,
        "SEMIANNUALY": 182.625,
        "ANNUALLY": 365.25
    }

    def calcResetDateTime(rFreq=ResetFrequency.DAILY, lastResetDate=datetime.now().date()):
        # ToDo: calculate timedelta for "WEEKDAY" and "WORKWEEKLY" ResetFrequency (?)

        # if the current reset date has passed, we calculate what the next one should be,
        # otherwise, we keep the current one
        if currentResetDateTime <= datetime.now():
            # the current reset date has passed...
            deltaDays = Task.day_counts[rFreq.name]
            nextDateTime = currentResetDateTime
            while nextDateTime.date() <= datetime.now().date():
                nextDateTime = datetime.combine(nextDateTime.date() + timedelta(days=deltaDays), datetime.min.time())
        else:
            # the current reset date is in the future...
            nextDateTime = currentResetDateTime
        return nextDateTime
```

Now reset date calculation is working (except for "WEEKDAY" and "WORKWEEKLY", which I will work on at some point in the future; not sure how useful those will really be). 

Next task is to integrate the reset date calculation into 'housekeeping' and reset the time duration for the current period as appropriate.

## 2025-10-03: (Friday)
Added code to 'newTaskFromDictionary()' to check for expired period and reset last session duration and period duration to 0.0.

## 2025-10-04: (Saturday)
Today's task (not pun intended): work on sorting the stack of task buttons so that they are in the order that they 'should' be done, with the most pressing at the top. Of course, this means I have to define the algorithm that determines what that order is... hmmm...

