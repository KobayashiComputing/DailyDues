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




