import tkinter as tk
import tkinter.messagebox as mb
from tkinter import scrolledtext
import psycopg2
import datetime
import os
import requests
from bs4 import BeautifulSoup

def clicked():
    username = username_entry.get()
    password = password_entry.get()
    host = host_entry.get()
    port = port_entry.get()
    db_name = db_name_entry.get()

    con = psycopg2.connect(
        database=db_name,
        user=username,
        password=password,
        host=host,
        port=port
    )

    if username == '' or password == '' or host == '' or port == '' or db_name == '':
        mb.showerror(title='Ошибка', message='Неправильно введены данные')
    else:
        #window.withdraw()
        new_window = tk.Tk()
        new_window.wm_attributes("-topmost", 1)
        new_window.title('Парсер vz.ru')
        new_window.geometry('450x450')
        new_main_label = tk.Label(new_window, text='Введите SQL запрос', font=('Arial', 13), **header_padding)
        new_main_label.pack()

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

        def parser():
            url = 'http://vz.ru'
            page = requests.get(url)
            print(page.status_code)  # статус код = 200 --> подключено
            soup = BeautifulSoup(page.text, 'html.parser')

            main_all = soup.findAll(name='div', class_='mainnews')
            oth_all = soup.findAll(name='div', class_='othnews')
            top_all = soup.findAll(name='td', class_='top')
            hour_all = soup.findAll(name='dt')
            o = 0
            date_time = datetime.datetime.now()
            format_date_time = date_time.strftime('%d.%m.%Y_%H.%M.%S')
            date_time_for_file = date_time.strftime('%d.%m.%Y')
            if os.path.exists("C:\parser"):
                exists = 1
            else:
                os.mkdir("C:\parser")
            if os.path.exists("C:\parser\_topnews_"):
                topnews_path = 'C:\parser\_topnews_'
            else:
                os.mkdir("C:\parser\_topnews_")
                mainnews_path = 'C:\parser\_topnews_'
            if os.path.exists("C:\parser\_mainnews_"):
                mainnews_path = 'C:\parser\_mainnews_'
            else:
                os.mkdir("C:\parser\_mainnews_")
                topnews_path = 'C:\parser\_mainnews_'
            if os.path.exists("C:\parser\_othnews_"):
                othnews_path = 'C:\parser\_othnews_'
            else:
                os.mkdir("C:\parser\_othnews_")
                othnews_path = 'C:\parser\_othnews_'
            if os.path.exists("C:\parser\_hournews_"):
                hournews_path = 'C:\parser\_hournews_'
            else:
                os.mkdir("C:\parser\_hournews_")
                hournews_path = 'C:\parser\_hournews_'

            news_block = []

            fullpath_topnews = os.path.join(topnews_path, format_date_time)
            os.mkdir(fullpath_topnews)
            for data in top_all:
                if data.find('a') is not None:

                    link = data.find('a')
                    news_link = 'https://vz.ru' + link.get('href')  # ссылка на новость

                    pr_link = link.text
                    res_link = pr_link.replace(':', '')

                    file_name = res_link  # имя файла
                    fullpath_topnews_file = os.path.join(fullpath_topnews,
                                                         file_name)  # объеденинение для описания пути к создающемуся файлу
                    my_file = open(fullpath_topnews_file + ".txt", "w+")  # открыть файл для записи

                    my_file.write(link.text)  # запись названия в файл
                    my_file.write('\n' + date_time_for_file)

                    news_page = requests.get(news_link)  # для парсинга страницы самой новости
                    news = BeautifulSoup(news_page.text, 'html.parser')
                    p_all = news.find(name='div', class_='text newtext')  # теги для поиска текста
                    for p in p_all:  # текст новости
                        if p.find('b') is not None:
                            my_file.write(p.text)
                        if p.find('p') is not None:
                            my_file.write(p.text)
                        o = o + 1

                    cur.execute(
                        "INSERT INTO TOPNEWS (NAME,FILE) VALUES (%s, %s)", (link.text, fullpath_topnews_file)
                    )
                    con.commit()

                    news_page = None
                    news_link = None

                    my_file.close()

            fullpath_mainnews = os.path.join(mainnews_path, format_date_time)
            os.mkdir(fullpath_mainnews)

            for data in main_all:
                if data.find(name='h1') is not None:
                    link = data.find('a')

                    # add_text = news_block.find(name='a', class_='text')
                    # print(add_text.text)  # текст начала статьи
                    news_link = 'https://vz.ru' + link.get('href')  # ссылка на статью

                    pr_link = link.text
                    res_link = pr_link.replace(':', '')

                    file_name = res_link  # имя файла
                    fullpath_mainnews_file = os.path.join(fullpath_mainnews,
                                                          file_name)  # объеденинение для описания пути к создающемуся файлу
                    my_file = open(fullpath_mainnews_file + ".txt", "w+")  # открыть файл для записи

                    my_file.write(link.text)  # запись названия в файл
                    my_file.write('\n' + date_time_for_file)

                    news_block = data
                    news_page = requests.get(news_link)  # для парсинга страницы самой новости
                    news = BeautifulSoup(news_page.text, 'html.parser')
                    p_all = news.find(name='div', class_='text newtext')  # теги для поиска текста

                    for p in p_all:  # текст новости
                        if p.find('b') is not None:
                            my_file.write(p.text)
                        if p.find('p') is not None:
                            my_file.write(p.text)
                        o = o + 1

                    cur.execute(
                        "INSERT INTO MAINNEWS (NAME,FILE) VALUES (%s, %s)", (link.text, fullpath_mainnews_file)
                    )
                    con.commit()

                    news_page = None
                    news_link = None

                    my_file.close()

            fullpath_othnews = os.path.join(othnews_path, format_date_time)
            os.mkdir(fullpath_othnews)

            for data in oth_all:  # пока нет кода для strong class
                if data.find(name='h4') is not None:
                    news_block = data
                    link = data.find('a')

                    oth_news_h4 = news_block.findAll(name='h4')
                    oth_news_h5 = news_block.findAll(name='h5')
                    oth_news_div = news_block.findAll('div')
                    # print(news_block)

                    for h4 in oth_news_h4:
                        if h4.find('a') is not None:
                            link = h4.find('a')
                            filename = link.text
                            news_link = 'https://vz.ru' + link.get('href')

                    pr_link = link.text
                    res_link = pr_link.replace(':', '')

                    file_name = res_link  # имя файла
                    fullpath_othnews_file = os.path.join(fullpath_othnews,
                                                         file_name)  # объеденинение для описания пути к создающемуся файлу
                    my_file = open(fullpath_othnews_file + ".txt", "w+")  # открыть файл для записи

                    my_file.write(link.text)  # запись названия в файл
                    my_file.write('\n' + date_time_for_file)

                    name_of_f = link.text
                    theme = None

                    for h5 in oth_news_h5:
                        if h5.find('a') is not None:
                            theme = h5.text
                            my_file.write(theme)

                    news_page = requests.get(news_link)  # для парсинга страницы самой новости
                    news = BeautifulSoup(news_page.text, 'html.parser')
                    p_all = news.find(name='div', class_='text newtext')  # теги для поиска текста
                    for p in p_all:  # текст новости
                        if p.find('b') is not None:
                            my_file.write(p.text)
                        if p.find('p') is not None:
                            my_file.write(p.text)
                        o = o + 1

                    news_page = None
                    news_link = None
                    comments = None

                    my_file.write('\nДополнительные материалы:')
                    count_materials = 0
                    for n in oth_news_div:
                        if n.find(name='strong', class_='material-type') is not None:
                            material_type = n.find(name='strong', class_='material-type').text
                            link = n.find('a')
                            comments = n.find(name='span', class_='material-title').text
                            n_link = link.get('href')

                            my_file.write(material_type)
                            my_file.write(comments)

                            count_materials = 0
                            if material_type != 'Интервью:':
                                if n_link[0] == 'h':
                                    count_materials += 1
                                    news_page = requests.get(n_link)  # для парсинга страницы самой новости
                                    news = BeautifulSoup(news_page.text, 'html.parser')
                                    p_all = news.find(name='div', class_='text newtext')  # теги для поиска текста
                                    for p in p_all:  # текст новости
                                        if p.find('b') is not None:
                                            my_file.write(p.text)
                                        if p.find('p') is not None:
                                            my_file.write(p.text)
                                        o = o + 1
                                    n_page = None
                                    n_link = None
                                else:
                                    continue
                    cur.execute(
                        "INSERT INTO OTHNEWS (NAME,FILE,KATEGORY,COMMENTS) VALUES (%s, %s, %s, %s)",
                        (name_of_f, fullpath_othnews_file, theme, comments)
                    )
                    con.commit()

                    my_file.close()

            fullpath_hournews = os.path.join(hournews_path, format_date_time)
            os.mkdir(fullpath_hournews)
            for data in hour_all:
                if data.find('span') is not None:
                    news_time = data.find('span').text
                    link = data.find('a')
                    news_link = 'https://vz.ru' + link.get('href')
                    pr_link = link.text
                    res_link = pr_link.replace(':', '')

                    file_name = res_link  # имя файла
                    fullpath_hourall_file = os.path.join(fullpath_hournews,
                                                         file_name)  # объеденинение для описания пути к создающемуся файлу
                    my_file = open(fullpath_hourall_file + ".txt", "w+")  # открыть файл для записи

                    my_file.write(link.text)  # запись названия в файл
                    my_file.write('\n' + date_time_for_file)
                    my_file.write('\n'+ news_time)
                    news_page = requests.get(news_link)  # для парсинга страницы самой новости
                    news = BeautifulSoup(news_page.text, 'html.parser')
                    b_all = news.find(name='div', class_='text newtext')  # теги для поиска текста
                    for b in b_all:  # текст новости
                        if b.find('b') is not None:
                            my_file.write(b.text)
                        if b.find('p') is not None:
                            my_file.write(b.text)
                        o = o + 1

                    cur.execute(
                        "INSERT INTO HOURNEWS (NAME,FILE) VALUES (%s, %s)", (link.text, fullpath_hourall_file)
                    )
                    con.commit()

                    news_page = None
                    news_link = None

                    my_file.close()
            #con.close()
        parser()

        def sql_clicked():
            sql = sql_entry.get()
            print(sql)
            cur.execute(sql)
            final = cur.fetchall()
            for fin in final:
                count = 0
                print(fin[count])
                count += 1
            con.commit()

        sql_entry = tk.Entry(new_window, width=40, bg='#fff', fg='#444', font=font_entry)
        sql_entry.pack()

        sql_btn = tk.Button(new_window, text='Выполнить', command=sql_clicked)
        sql_btn.pack(**base_padding)

        result_label = tk.Label(new_window, text='Вывод: ', font=label_font, **base_padding)
        result_label.pack()

        result = scrolledtext.ScrolledText(new_window, width=40, height=15, bg="#fff", fg='#444')
        result.pack()

        con.commit()
        #cur.close()
        #con.close()
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

main_label = tk.Label(window, text='Аутентификация', font=font_header, **header_padding)
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
password_entry = tk.Entry(window, show='*', bg='#fff', fg='#444', font=font_entry)
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