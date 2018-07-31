# Creating yhr GUI Form and Adding Widgets

'''
Contents:
- Creating our first Python GUI
- Preventing the GUI from being resized
- Adding a label to the GUI form
- Creating buttons and changing their text property
- Text box widgets
- Setting the focus on a widget and disabling widgets
- Combo box widgets
- Creating a check button with different initial states
- Using radio button widgets
- Using scrolled text widgets
- Adding several widgets in a loop
'''

## Creating the first Python GUI
# import tkinter as tk 
# win = tk.Tk() # create an instance of `Tk` class
# win.title("Python GUI") # set value for `title` property of win
# win.mainloop() # Start the main event loop and display window

'''
A event loop is a mechanism that makes out GUI work. We can think of it as an endless loop where our GUI is waiting for events to be sent to it.

The event loop ends when the user click the red x button or a widget that we have programmed to end our GUI. When the event loop ends, our GUI also ends.
'''

# Preventing the GUI from being resized

# import tkinter as tk 
# win = tk.Tk()
# win.title("Python GUI")
# win.resizable(0, 0)
# win.mainloop()

'''
`Resizable()` is a method of the `Tk()` class and, by passing (0,0), we prevent the GUI from being resized. If we pass in other values, we hard-code the x and y start up size of the GUI, but that won't make it nonresizable.
'''

# Adding a label to the GUI form

# import tkinter as tk 
# from tkinter import ttk 
# win = tk.Tk()
# win.title("Python GUI")
# ttk.Label(win, text="A Label").grid(column=0, row=0)
# win.mainloop()

'''
`ttk` stands for 'themed tk'. It improves our GUI look and feel.

we pass out window instance into the `ttk.Label` constructor and set the text property. we also make use of the grid layout manager.
'''

# Creating buttons and changing their text property

import tkinter as tk 
from tkinter import ttk 
win = tk.Tk()
win.title("Python GUI")

aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text="**I have been Clicked!**")
    aLabel.configure(foreground='red')

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)

win.mainloop()

'''
we create a button object and bind the `clickMe()` function to it.

Guis are event-driven. Clicking the button creates an event. We bind what happens when this event occurs in the callback function using the command property of the `ttk.Button` widget.
'''

# Text box widgets



