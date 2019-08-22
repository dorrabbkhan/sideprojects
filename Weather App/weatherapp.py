"""
Simple weather application built in Tkinter
"""

import tkinter as tk


HEIGHT = 400
WIDTH = 600


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
# create root and canvas

frame = tk.Frame(root, bg='blue')
frame.place(relwidth=1, relheight=1)
# create main frame

label = tk.Label(frame, text="This is a label", bg='gray')
label.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)
entry = tk.Entry(frame, bg='white')
entry.place(relx=0, rely=0, relwidth=0.8, relheight=0.1)
button = tk.Button(root, text="Text Button", bg='black', fg='white', bd=5)
button.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)
# create label, entry and button

root.mainloop()
# make window
