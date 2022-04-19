import math
import tkinter as tk

window = tk.Tk()
word = tk.Label(text = "Введите цифры")
word.pack()

button = tk.Button(
    text = "Старт",
    width = 15,
    height = 5,
    bg = "black",
    fg = "white",
)
button.pack()

entry1 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry1.pack()
entry2 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry2.pack()
entry3 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry3.pack()
entry4 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry4.pack()
entry5 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry5.pack()
entry6 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry6.pack()
entry7 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry7.pack()
entry8 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry8.pack()
entry9 = tk.Entry(fg = "black", bg = "white", width = 20)  #.get()
entry9.pack()

window.mainloop()