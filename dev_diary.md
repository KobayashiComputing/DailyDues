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


