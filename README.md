# tkopen
Simple file launcher for Linux using Python3's tkinter.
(There's probably a better term but I can't think of one)

# Installation
Currently, you would need to improvise, adding a shell script to your path which executes main.py.
Also be sure to add the config file in ~/.config/tkopen/ (config file should be named "directories", though that'll probably change soon)

Example config:
```
/home/user/foo
/home/guest/scripts

```
# Future plans:
-Add scrolling
-Allow users to add icons to folders in the config
-Refine the way files are opened
-Stop using the "pack" function and instead use "grid" (see main.py for context)
