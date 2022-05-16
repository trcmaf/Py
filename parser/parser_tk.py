import tkinter as tk
import tkinter.messagebox as mb
import psycopg2

def clicked():
    username = username_entry.get()
    password = password_entry.get()
    host = host_entry.get()
    port = port_entry.get()
    db_name = db_name_entry.get()

    if username == '' or password == '' or host == '' or port == '' or db_name == '':
        mb.showerror(title='Ошибка', message='Неправильно введены данные')
    else:
        window.withdraw()
        new_window = tk.Tk()
        new_window.wm_attributes("-topmost", 1)
        new_window.title('Парсер vz.ru')
        new_window.geometry('450x450')
        new_main_label = tk.Label(new_window, text='Введите SQL запрос', font=font_header, **header_padding)
        new_main_label.pack()
        con = psycopg2.connect(
            database=db_name,
            user=username,
            password=password,
            host=host,
            port=port
        )
        print("Database opened successfully")
        cur = con.cursor()
        cur.execute('''DROP TABLE IF EXISTS MAINNEWS''')
        cur.execute('''DROP TABLE IF EXISTS HOURNEWS''')
        cur.execute('''DROP TABLE IF EXISTS TOPNEWS''')
        cur.execute('''DROP TABLE IF EXISTS OTHNEWS''')
        cur.execute('''CREATE TABLE MAINNEWS (NAME TEXT NOT NULL, FILE TEXT);''')
        print("Table MAINNEWS created succcessfully")
        cur.execute('''CREATE TABLE HOURNEWS (NAME TEXT NOT NULL, FILE TEXT);''')
        print("Table HOURNEWS created succcessfully")
        cur.execute('''CREATE TABLE TOPNEWS (NAME TEXT NOT NULL, FILE TEXT);''')
        print("Table TOPNEWS created succcessfully")
        cur.execute('''CREATE TABLE OTHNEWS (NAME TEXT NOT NULL, FILE TEXT, KATEGORY TEXT, COMMENTS TEXT);''')
        print("Table OTHNEWS created succcessfully")

        #new_window.protocol("WM_DELETE_WINDOW", window.destroy())
        new_window.mainloop()


window = tk.Tk()
window.title('Парсер vz.ru')
window.geometry('450x450')
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

main_label = tk.Label(window, text='Авторизация', font=font_header, **header_padding)
main_label.pack()

# метка для поля ввода имени
username_label = tk.Label(window, text='Имя пользователя: ', font=label_font , **base_padding)
username_label.pack()
# поле ввода имени
username_entry = tk.Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# метка для поля ввода пароля
password_label = tk.Label(window, text='Пароль: ', font=label_font , **base_padding)
password_label.pack()
# поле ввода пароля
password_entry = tk.Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()

# метка для поля ввода host
host_label = tk.Label(window, text='Host: ', font=label_font , **base_padding)
host_label.pack()
# поле ввода host
host_entry = tk.Entry(window, bg='#fff', fg='#444', font=font_entry)
host_entry.pack()

# метка для поля ввода port
port_label = tk.Label(window, text='Порт: ', font=label_font , **base_padding)
port_label.pack()
# поле ввода port
port_entry = tk.Entry(window, bg='#fff', fg='#444', font=font_entry)
port_entry.pack()

# метка для поля ввода названия БД
db_name_label = tk.Label(window, text='Имя БД: ', font=label_font , **base_padding)
db_name_label.pack()
# поле ввода названия БД
db_name_entry = tk.Entry(window, bg='#fff', fg='#444', font=font_entry)
db_name_entry.pack()

# кнопка отправки формы
send_btn = tk.Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

window.mainloop()




#---------------------------------------
# window = tk.Tk()
#
# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()
# width = round(width / 3)
# height = round(height / 3)
# window.geometry('350x150+{}+{}'.format(width, height))
# window.title("Парсер vz.ru")
#
# label = tk.Label(window, text = "Выберите тему:", font= ("Arial", 13))
# #label.grid(column = 0, row = 0)
# label.pack()
#
# themes = ['Экономика', 'Политика', 'Общество']
# end = len(themes)
# listb = tk.Listbox(height = end)
# for i in themes:
#     listb.insert(end, i)
# #listb.bind("<<ListboxSelect>>", self.onSelect)
# listb.pack(pady=15)
#
# def click():
#     mb.showinfo("Внимание","Данные будут сохранены в БД")
# button = tk.Button(window, text = 'Ок', command = click)
# #button.grid(column = 0, row = 1)
# button.pack()
#
#window.mainloop()