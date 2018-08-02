# Layout Management

'''
- Arranging several labels within a label frame widget
- Using padding to add space around widgets
- How widgets dynamically expand the GUI
- Aligning the GUI widgets by embedding frames within frames
- Creating menu bars
- Creating tabbed widgets
- Using the grid layout manager

The grid layout manager is one of the most important layout tools built into tkinter that we will be using.
'''

# Arranging several labels within a label frame widget

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
#     aButton.configure(text=name.get() +' '+ number.get())
# aButton = ttk.Button(win, text='Click Me!', command=clickMe)
# aButton.grid(column=2, row=1)

# chVar1 = tk.IntVar()
# chBtn1 = tk.Checkbutton(win, text='Disabled', state='disabled', variable=chVar1)
# chBtn1.select()
# chBtn1.grid(column=0, row=2)
# chVar2 = tk.IntVar()
# chBtn2 = tk.Checkbutton(win, text='Unchecked', variable=chVar2)
# chBtn2.deselect()
# chBtn2.grid(column=1, row=2) 
# chVar3 = tk.IntVar()
# chBtn3 = tk.Checkbutton(win, text='Toggle', variable=chVar3)
# chBtn3.select() 
# chBtn3.grid(column=2, row=2) 

# # scrollVar = tk.StringVar()
# scr = scrolledtext.ScrolledText(win, width=50, height=6, wrap=tk.WORD)
# scr.grid(column=0, columnspan=3)

# COLOR1 = 'Blue'
# COLOR2 = 'Gold'
# COLOR3 = 'Red'
# radVar = tk.IntVar()
# def radCall():
#     radSel = radVar.get()
#     if radSel==1: win.configure(background=COLOR1)
#     elif radSel==2: win.configure(background=COLOR2)
#     elif radSel==3: win.configure(background=COLOR3)
# radBtn1 = tk.Radiobutton(win, text=COLOR1, value=1, variable=radVar, command=radCall)
# radBtn1.grid(column=0, row=4)
# radBtn2 = tk.Radiobutton(win, text=COLOR2, value=2, variable=radVar, command=radCall)
# radBtn2.grid(column=1, row=4)
# radBtn3 = tk.Radiobutton(win, text=COLOR3, value=3, variable=radVar, command=radCall)
# radBtn3.grid(column=2, row=4) 


# labelsFrame = ttk.LabelFrame(win, text=' Labels in a Frame ')
# labelsFrame.grid(column=0, row=5) 
# ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
# ttk.Label(labelsFrame, text='Label2').grid(column=1, row=0)
# ttk.Label(labelsFrame, text='Label3').grid(column=2, row=0)

# labelsFrame2 = ttk.LabelFrame(win, text=' Labels in a Frame ')
# labelsFrame2.grid(column=2, row=5) 
# ttk.Label(labelsFrame2, text='Label1').grid(column=0, row=0)
# ttk.Label(labelsFrame2, text='Label2').grid(column=0, row=1)
# ttk.Label(labelsFrame2, text='Label3').grid(column=0, row=2)
# ttk.Button(labelsFrame2, text='ClickMe').grid(column=0, row=3)

# nameEntry.focus()
# win.mainloop()


# Using padding to add space around widgets
# import tkinter as tk 
# from tkinter import ttk 
# win = tk.Tk()
# win.title("Python GUI")

# labelsFrame = ttk.LabelFrame(win, text=' Labels in a Frame ')
# labelsFrame.grid(column=0, row=0, padx=20, pady=20)
# ttk.Label(labelsFrame, text='label1').grid(column=0, row=0)
# ttk.Label(labelsFrame, text='label2').grid(column=0, row=1)
# ttk.Label(labelsFrame, text='label3').grid(column=0, row=2)
# for child in labelsFrame.winfo_children():
#     child.grid_configure(padx=8, pady=4)

# win.mainloop()

'''
In tkinter, adding space horizontally and vertically is done by using the built-in properties named `padx`, and `pady`.

we can use a loop to add space around the labels contained within the labelFrame. The `winfo_children()` functionreturns a list of all the children belonging to the `labelFrame` variable. This enables us to loop through them and assign the padding to each label.

The `grid_configure()` function enables us to modify the UI elements before the main loop displays them. So, instead of hard-coding values when we first create a widget, we can work on our layout and then arrange spacing towards the end of our file, juse before the GUI is being created. This is a neat technique to know. 
'''

# How widgets dynamically expand the GUI
# 主要介绍了一些自动对齐的机制

# Aligning the GUI widgets by embedding frames within frames

'''
The dynamic behavior of Python and its GUI modules can create a little bit of challenge to really get our GUI looking the way we want. Here we will embed frames within frames to get more control of our layout. 

To the end, we will have to embed our current controls within a central `ttk.LabelFrame`. This `ttk.LabelFrame` is a child of the main parent window and all controls will be children of this `ttk.LabelFrame`.
'''

# import tkinter as tk 
# from tkinter import ttk 
# win = tk.Tk()
# win.title("Python GUI")
# monty = ttk.LabelFrame(win, text='Monty Python')
# monty.grid(column=0, row=0) 

# ttk.Label(monty, text='Enter a name:').grid(column=0, row=0)
# ttk.Label(monty, text='Choose a number:').grid(column=1, row=0)
# name = tk.StringVar()
# nameEntry = ttk.Entry(monty, width=12, textvariable=name)
# nameEntry.grid(column=0, row=1) 
# number = tk.StringVar()
# numCombo = ttk.Combobox(monty, width=12, textvariable=number, state='readonly')
# numCombo['values']=(1, 2, 4, 42, 100)
# numCombo.grid(column=1, row=1)
# def clickMe():
#     aButton.configure(text=name.get()+' '+number.get())
# aButton = ttk.Button(monty, text='Click Me!', command=clickMe)
# aButton.grid(column=2, row=1)

# chVar1 = tk.IntVar()
# chBtn1 = tk.Checkbutton(monty, text='Disabled', state='disabled', variable=chVar1)
# chBtn1.select()
# chBtn1.grid(column=0, row=2, sticky=tk.W)
# chVar2 = tk.IntVar()
# chBtn2 = tk.Checkbutton(monty, text='Unchecked', variable=chVar2)
# chBtn2.deselect()
# chBtn2.grid(column=1, row=2, sticky=tk.W)
# chVar3 = tk.IntVar() 
# chBtn3 = tk.Checkbutton(monty, text='Toggle', variable=chVar3)
# chBtn3.select()
# chBtn3.grid(column=2, row=2, sticky=tk.W) 

# from tkinter import scrolledtext
# scr = scrolledtext.ScrolledText(monty, width=20, height=5)
# scr.grid(column=0, columnspan=3, row=3, sticky='WE')

# COLOR1 = 'Blue'
# COLOR2 = 'Gold'
# COLOR3 = 'Red'
# radVar = tk.IntVar()
# def radCall():
#     radSel = radVar.get() 
#     if radSel==1: scr.configure(background=COLOR1)
#     elif radSel==2: scr.configure(background=COLOR2)
#     elif radSel==3: scr.configure(background=COLOR3)
# radBtn1 = tk.Radiobutton(monty, text=COLOR1, value=1, variable=radVar, command=radCall)
# radBtn1.grid(column=0, row=4, sticky=tk.W)
# radBtn2 = tk.Radiobutton(monty, text=COLOR2, value=2, variable=radVar, command=radCall)
# radBtn2.grid(column=1, row=4, sticky=tk.W) 
# radBtn3 = tk.Radiobutton(monty, text=COLOR3, value=3, variable=radVar, command=radCall)
# radBtn3.grid(column=2, row=4, sticky=tk.W) 

# labelsFrame = ttk.LabelFrame(monty, text=' Labels in a Frame ')
# labelsFrame.grid(columns=1, row=5)
# ttk.Label(labelsFrame, text='label 1').grid(column=0, row=0)
# ttk.Label(labelsFrame, text='label 2').grid(column=0, row=1)
# ttk.Label(labelsFrame, text='label 3').grid(column=0, row=2)

# for child in labelsFrame.winfo_children():
#     child.grid_configure(padx=4, pady=8)

# win.mainloop()

'''
We combined both 'W' and 'E' to make our ScrolledText widget attach itself both to the left and right sides of its container using 'WE'. We can add more combinations: 'NSE' will stretch our widget to the top, bottom and right side. If we have only one widget in using all options: "NSWE". We can also use tuple syntax: `sticky=(tk.N, tk.S, tk.W, tk.E)`.
'''

# Creating menu bars

# import tkinter as tk 
# from tkinter import ttk 
# from tkinter import scrolledtext
# from tkinter import Menu

# win = tk.Tk()
# win.title("Python GUI")
# monty = ttk.LabelFrame(win, text='Monty Python')
# monty.grid(column=0, row=0)

# scr = scrolledtext.ScrolledText(monty, width=50, height=10)
# scr.grid(column=0, row=0, stick='EW') 

# menuBar = Menu(win) 
# win.config(menu=menuBar)

# def _quit():
#     win.quit()
#     win.destroy()
#     exit() 

# fileMenu = Menu(menuBar) 
# fileMenu.add_command(label="New")
# fileMenu.add_separator() 
# fileMenu.add_command(label='Exit', command=_quit)
# menuBar.add_cascade(label='File', menu=fileMenu)

# helpMenu = Menu(menuBar, tearoff=0)
# helpMenu.add_command(label='About')
# menuBar.add_cascade(label='Help', menu=helpMenu)

# win.mainloop()

'''
目前 menu 中只有 Exit 真正起作用，但是 `_quit()` 似乎并没有完全释放资源，因为推出的时候会报错。
'''

# Creating tabbed widgets

import tkinter as tk 
from tkinter import ttk 
win = tk.Tk() 
win.title("Python GUI")
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill='both')

monty = ttk.LabelFrame(tab1, text=' Monty Python ')
monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')


monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
monty2.grid(column=0, row=0, padx=8, pady=4)
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty2, text='Disabled', variable=chVarDis, state='disabled')
check1.grid(column=0, row=0, sticky='W')

win.mainloop()

'''
While in previous recipes, we used the grid layout manager for simpler GUIs, we can use a simpler layout manager and "pack" is one of them. In the above code, we 'pack' tabControl ttk.Notebook into the main GUI form expanding the notebook tabbed control to fill in all sides.
'''