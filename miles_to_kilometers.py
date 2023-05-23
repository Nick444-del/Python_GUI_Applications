import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entryInt.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# windows
windows = ttk.Window(themename= 'journal')
windows.title('Miles to KM')
windows.geometry('400x200')

# title
title_label = ttk.Label(master = windows, text = 'Miles to kilomenters', font = 'Calibre 24 bold')
title_label.pack()

# input field
input_field = ttk.Frame(master = windows)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_field, textvariable = entryInt)
button = ttk.Button(master = input_field, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_field.pack(pady = '10')

# output
output_string = tk.StringVar()
output_label = ttk.Label(master = windows, text = 'Output', font='Calibri 24', textvariable= output_string)
output_label.pack(pady = 5)

# run
windows.mainloop()