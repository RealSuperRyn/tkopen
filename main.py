#!/usr/bin/python3

#Copyright 2023 SuperRyn
#    This program is free software: you can redistribute it and/or modify it under the
#	terms of the GNU General Public License as published by the Free Software
#	Foundation, either version 3 of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY
#	WARRANTY; without even the implied warranty of MERCHANTABILITY or
#	FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#	more details.
#   You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
from tkinter import *
from os.path import expanduser, isfile, exists
from os import listdir
from sys import exit
import subprocess

#Preparation to parse the config file
home = expanduser("~")
configfile = home + "/.config/tkopen/directories"
#Check if configuration file exists
if not (exists(configfile) and isfile(configfile)):
    error = Tk()
    message = Label(error, text="The configuration file does not exist or is a directory. \n The config file should be placed in ~/.config/tkopen/ and be named \"directories\"")
    message.pack()
    error.mainloop()
    exit(1)


#Tkinter boilerplate
rootWindow = Tk()

#Button logic
files = []
names = []
def dodir(index):
    print("Unimplemented.")
    print("Debug info: " + str(index) + " " + str(paths))
    for widget in rootWindow.winfo_children():
        widget.destroy()
    undiscerned = listdir(paths[index])
    for f in undiscerned:
        if isfile(paths[index] + f):
            files.append(paths[index] + f)
            names.append(f)
    j = -1
    for f in files:
        j += 1
        Button(rootWindow, text=names[j], command=lambda x=j: dofile(x)).pack()

def dofile(index):
    #Easy as pie... for now.
    subprocess.call(('xdg-open', files[index]))

#Parsing the configuration file and populating buttons
config = open(configfile, "r").read().split("\n")
config.pop(len(config) - 1)

i = 0
paths = []
icons = []
while i < len(config):
    #icons.append(config[i]) Will implement icons later on.
    paths.append(config[i])
    i += 1

j = -1
for i in paths:
    j += 1
    Button(rootWindow, text=i, command=lambda x=j: dodir(x)).pack()

rootWindow.mainloop()
