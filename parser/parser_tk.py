import tkinter as tk, tkinter as mb

window = tk.Tk()

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
width = round(width / 3)
height = round(height / 3)
window.geometry('350x150+{}+{}'.format(width, height))
window.title("Парсер vz.ru")

label = tk.Label(window, text = "Выберите тему:", font= ("Arial", 13))
#label.grid(column = 0, row = 0)
label.pack()

themes = ['Экономика', 'Политика', 'Общество']
end = len(themes)
listb = tk.Listbox(height = end)
for i in themes:
    listb.insert(end, i)
#listb.bind("<<ListboxSelect>>", self.onSelect)
listb.pack(pady=15)

def click():
    mb.showinfo("Внимание","Данные будут сохранены в БД")
button = tk.Button(window, text = 'Ок', command = click)
#button.grid(column = 0, row = 1)
button.pack()

window.mainloop()