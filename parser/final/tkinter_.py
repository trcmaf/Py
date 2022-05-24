import tkinter_ as tk
import tkinter_.messagebox as mb

window = tk.Tk()
window.title('Авторизация')
window.geometry('450x230')
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

# обработчик нажатия на клавишу 'Войти'
def clicked():
    # получаем имя пользователя и пароль
    username = username_entry.get()
    password = password_entry.get()
    host = host_entry.get()
    port = port_entry.get()
    db_name = db_name_entry.get()

    # выводим в диалоговое окно введенные пользователем данные
    mb.showinfo('Заголовок', '{username}, {password}'.format(username=username, password=password))


# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# для всех остальных виджетов настройки делаются также
main_label = tk.Label(window, text='Авторизация', font=font_header, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
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


# запускаем главный цикл окна
window.mainloop()
