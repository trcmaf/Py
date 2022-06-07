import tkinter as tk


new_window = tk.Tk()
new_window.wm_attributes("-topmost", 1)
new_window.title('Парсер vz.ru')
new_window.geometry('600x450')
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}
font_entry = ('Arial', 12)
new_main_label = tk.Label(new_window, text='Введите SQL запрос', font=('Arial', 13), **header_padding)
new_main_label.pack()
sql_entry = tk.Entry(new_window, width=40, bg='#fff', fg='#444', font=font_entry)
sql_entry.pack()

sql_btn = tk.Button(new_window, text='Выполнить')
sql_btn.pack(**base_padding)
result_label = tk.Label(new_window, text='Вывод: ', font=label_font, **base_padding)
result_label.pack()
new_window.mainloop()