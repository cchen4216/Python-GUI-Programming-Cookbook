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

# import tkinter as tk 
# from tkinter import ttk 
# win = tk.Tk()
# win.title("Python GUI")

# aLabel = ttk.Label(win, text="A Label")
# aLabel.grid(column=0, row=0)

# def clickMe():
#     action.configure(text="**I have been Clicked!**")
#     aLabel.configure(foreground='red')

# action = ttk.Button(win, text="Click Me!", command=clickMe)
# action.grid(column=1, row=0)

# win.mainloop()

'''
we create a button object and bind the `clickMe()` function to it.

Guis are event-driven. Clicking the button creates an event. We bind what happens when this event occurs in the callback function using the command property of the `ttk.Button` widget.
'''

# Text box widgets

# import tkinter as tk 
# from tkinter import ttk 

# win = tk.Tk()
# win.title("Python GUI")

# aLabel = ttk.Label(win, text='Enter you Name:')
# aLabel.grid(column=0, row = 0)

# name = tk.StringVar()
# nameEntry = ttk.Entry(win, width=12, textvariable=name)
# nameEntry.grid(column=0, row=1)

# def clickMe():
#     aButton.configure(text='Hi, '+name.get())
# aButton = ttk.Button(win, text='ClickMe!', command=clickMe)
# aButton.grid(column=1, row=1)

# win.mainloop()

'''
Notice, the button click event is a callback function, that is, the value of `command` is `clickMe` instead of `clickMe()`.

Using tkinter, we have to declare the variable `name` as the type `tk.StringVar()` before we can use it sucessfully. The reason is this that Tkinter is not Python. We can use it from Python but it is not the same lanuage.
'''

# Setting the focus to a widget and disabling widgets

# import tkinter as tk 
# from tkinter import ttk 

# win = tk.Tk()
# win.title("Python GUI")

# aLabel = ttk.Label(win, text='Enter your name:')
# aLabel.grid(column=0, row=0)

# name = tk.StringVar()
# nameEntry = ttk.Entry(win, width=12, textvariable=name)
# nameEntry.grid(column=0, row=1)

# def clickMe():
#     aButton.configure(text='Hi, ' + name.get())
#     aButton.configure(state='disable')
# aButton = ttk.Button(win, text='clickMe', command=clickMe)
# aButton.grid(column=1, row=1)

# nameEntry.focus()
# win.mainloop()

'''
上面的代码运行之后，就可以直接在 nameEntry 内输入字符了，而不需要鼠标先点上。输入完文字后，点击 button，button 的 text 会变化，并且 button 不能再点了。
'''

# Combo box widgets

# import tkinter as tk 
# from tkinter import ttk 
# win = tk.Tk()
# win.title("Python GUI")

# aLabel = ttk.Label(win, text='Enter a name:')
# aLabel.grid(column=0, row=0)
# name = tk.StringVar()
# nameEntry = ttk.Entry(win, width=12, textvariable=name)
# nameEntry.grid(column=0, row=1)

# numLabel = ttk.Label(win, text='Choose a number:')
# numLabel.grid(column=1, row=0)
# number = tk.StringVar()
# numberChosen = ttk.Combobox(win, width=12, textvariable=number)
# numberChosen['values'] = (1, 2, 4, 42, 100)
# numberChosen.grid(column=1, row=1)
# numberChosen.current(0)

# def clickMe():
#     aButton.configure(text=number.get())
# aButton = ttk.Button(win, text='ClickMe!', command=clickMe)
# aButton.grid(column=2, row=1)

# win.mainloop()

'''
上面的代码运行后，你既可以从下拉列表中选择一个数值，也可以手动输入一个。如果不想让用户自己输入数值的话，可以设置 Combobox state 为 readonly

numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
'''

# Creating a check button with different initial states

# import tkinter as tk 
# from tkinter import ttk 
# win = tk.Tk()
# win.title("Python GUI")

# nameLabel = ttk.Label(win, text='Enter a name:')
# nameLabel.grid(column=0, row=0)
# numLabel = ttk.Label(win, text='Choose a number:')
# numLabel.grid(column=1, row=0)

# name = tk.StringVar()
# nameEntry = ttk.Entry(win, width=12, textvariable=name)
# nameEntry.grid(column=0, row=1)
# number = tk.StringVar()
# numCombo = ttk.Combobox(win, width=12, textvariable=number)
# numCombo['values'] = (1, 2, 4, 42, 100)
# numCombo.grid(column=1, row=1)

# def clickMe():
#     aButton.configure(text=name.get() + ' ' + number.get())
# aButton = ttk.Button(win, text='Click Me!', command=clickMe)
# aButton.grid(column=2, row=1)

# chVarDis = tk.IntVar()
# check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
# check1.select()
# check1.grid(column=0, row=2, sticky=tk.W)

# chVarUn = tk.IntVar()
# check2 = tk.Checkbutton(win, text='UnChecked', variable=chVarUn)
# check2.deselect()
# check2.grid(column=1, row=2, sticky=tk.W)

# chVarEn = tk.IntVar()
# check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
# check3.select()
# check3.grid(column=2, row=2, sticky=tk.W)

# win.mainloop()

'''
We place these `Checkbutton` widgets in our main window so the first argument passed into the constructor is the parent of the widget; in our case `win`.

Setting the sticky property of the grid to `tk.W` means that the widget will be aligned to the west of the grid.
'''

# Using radio button widgets

# import tkinter as tk 
# from tkinter import ttk 
# win = tk.Tk()
# win.title('Python GUI')

# ttk.Label(win, text='Enter a name:').grid(column=0, row=0)
# ttk.Label(win, text='Choose a number:').grid(column=1, row=0)

# name = tk.StringVar()
# nameEntry = ttk.Entry(win, width=12, textvariable=name)
# nameEntry.grid(column=0, row=1)

# number = tk.StringVar()
# numCombo = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
# numCombo['values'] = (1, 2, 4, 42, 100)
# numCombo.current(2)
# numCombo.grid(column=1, row=1) 

# def clickMe():
#     aButton.configure(text=name.get()+' '+number.get())
# aButton = ttk.Button(win, text='Click Me!', command=clickMe)
# aButton.grid(column=2, row=1)

# chVar1 = tk.IntVar()
# chButton1 = tk.Checkbutton(win, text='Disabled', variable=chVar1, state='disabled')
# chButton1.select()
# chButton1.grid(column=0, row=2, sticky=tk.W)

# chVar2 = tk.IntVar()
# chButton2 = tk.Checkbutton(win, text='Unchecked', variable=chVar2)
# chButton2.deselect()
# chButton2.grid(column=1, row=2, sticky=tk.W)

# chVar3 = tk.IntVar()
# chButton3 = tk.Checkbutton(win, text='Enabled', variable=chVar3)
# chButton3.select()
# chButton3.grid(column=2, row=2, sticky=tk.W)

# COLOR1 = 'Blue'
# COLOR2 = 'Gold'
# COLOR3 = 'Red'
# def radCall():
#     radSel = radVar.get()
#     if radSel == 1: win.configure(background=COLOR1)
#     elif radSel == 2: win.configure(background=COLOR2)
#     elif radSel == 3: win.configure(background=COLOR3)
# radVar = tk.IntVar()
# rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
# rad1.grid(column=0, row=3, sticky=tk.W)

# rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
# rad2.grid(column=1, row=3, sticky=tk.W)

# rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
# rad3.grid(column=2, row=3, sticky=tk.W) 

# win.mainloop()

'''
By assigning the name of the color to a variable and using this variable in several places, we can easily experiment with different colors. Instead of doing a global search-and-replace of a hard-coded string (which is prone to errors), we just need to change one line of code and everything else will work. This is known as the **DRY principle**, which stands for **Don't Repeat Yourself**.

We created one `tk.IntVar` variable. What is important about this is that we are creating only one variable to be used by all three radio buttons. As can be seen from the above screenshot, no matter which `Radiobutton` we select, all the others will automatically be unselected for us.
'''

# Using scrolled text widgets

# import tkinter as tk 
# from tkinter import ttk 
# from tkinter import scrolledtext

# win = tk.Tk()
# win.title("Python GUI")

# ttk.Label(win, text='Enter a name:').grid(column=0, row=0)
# ttk.Label(win, text='Choose a number:').grid(column=1, row=0)
# name = tk.StringVar()
# nameEntry = ttk.Entry(win, width=12, textvariable=name)
# nameEntry.grid(column=0, row=1)
# number = tk.StringVar()
# numCombo = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
# numCombo['values'] = (1, 2, 4, 42, 100)
# numCombo.grid(column=1, row=1)

# def clickMe():
#     pass
# aButton = ttk.Button(win, text='Click Me!', command=clickMe)
# aButton.grid(column=2, row=1)

# chVar1 = tk.IntVar()
# chBtn1 = tk.Checkbutton(win, text='Disabled', state='disabled', variable=chVar1)
# chBtn1.select()
# chBtn1.grid(column=0, row=2, sticky=tk.W)

# chVar2 = tk.IntVar()
# chBtn2 = tk.Checkbutton(win, text='Unchecked', variable=chVar2)
# chBtn2.deselect()
# chBtn2.grid(column=1, row=2, sticky=tk.W) 

# chVar3 = tk.IntVar()
# chBtn3 = tk.Checkbutton(win, text='Enabled', variable=chVar3)
# chBtn3.select()
# chBtn3.grid(column=2, row=2)

# COLOR1 = 'Blue'
# COLOR2 = 'Gold'
# COLOR3 = 'Red'
# radVar = tk.IntVar()
# def radCall():
#     radSel = radVar.get()
#     if radSel==1: win.configure(background=COLOR1)
#     elif radSel==2: win.configure(background=COLOR2)
#     elif radSel==3: win.configure(background=COLOR3)
# radBtn1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
# radBtn1.grid(column=0, row=3, sticky=tk.W)
# radBtn2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
# radBtn2.grid(column=1, row=3, sticky=tk.W)
# radBtn3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
# radBtn3.grid(column=2, row=3, sticky=tk.W)

# scrolW = 30
# scrolH = 5
# scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
# scr.grid(column=0, columnspan=3)

# win.mainloop()

'''
By setting the `wrap` property to `tk.WORD` we are telling the `ScrolledText` widget to break lines by words, so that we do not wrap around within a word. The default option is `tk.CHAR`, which wraps any character regardless of whether we are in the middle of a word.

Setting the `columnspan` property of the grid widget to 3 for the `ScrolledText` widget makes this widget span all three columns. If we did not set this property, our `ScrolledText` widget would only reside in column one, which is not what we want.
'''

# Adding several widgets in a loop

import tkinter as tk 
win = tk.Tk()
win.title("Python GUI")

colors = ['Blue', 'Gold', 'Red']
radVar = tk.IntVar()

def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col],
        variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=0, sticky=tk.W)

win.mainloop()
