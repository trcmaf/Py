import datetime
import DB
import os
import requests  # импорт библиотеки request
from bs4 import BeautifulSoup  # импорт библиотеки BeautifulSoup

url = 'http://vz.ru'  # ссылка на страницу сайта для парсинга
page = requests.get(url)
print(page.status_code)  # статус код = 200 --> подключено
soup = BeautifulSoup(page.text, 'html.parser')

main_all = soup.findAll(name='div', class_='mainnews')
oth_all = soup.findAll(name='div', class_='othnews')
top_all = soup.findAll(name='td', class_='top')
hour_all = soup.findAll(name='dt')  # раздел "Новости часа"
o = 0
date_time = datetime.datetime.now()
format_date_time = date_time.strftime('%d.%m.%Y_%H.%M.%S')
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

        news_page = requests.get(news_link)  # для парсинга страницы самой новости
        news = BeautifulSoup(news_page.text, 'html.parser')
        p_all = news.find(name='div', class_='text newtext')  # теги для поиска текста
        for p in p_all:  # текст новости
            if p.find('b') is not None:
                my_file.write(p.text)
            if p.find('p') is not None:
                my_file.write(p.text)
            o=o+1

        DB.cur.execute(
            "INSERT INTO TOPNEWS (NAME,FILE) VALUES (%s, %s)", (link.text, fullpath_topnews_file)
        )
        DB.con.commit()

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

        news_block = data
        news_page = requests.get(news_link)  # для парсинга страницы самой новости
        news = BeautifulSoup(news_page.text, 'html.parser')
        p_all = news.find(name='div', class_='text newtext')  # теги для поиска текста


        for p in p_all:  # текст новости
            if p.find('b') is not None:
                my_file.write(p.text)
            if p.find('p') is not None:
                my_file.write(p.text)
            o=o+1



        DB.cur.execute(
            "INSERT INTO MAINNEWS (NAME,FILE) VALUES (%s, %s)", (link.text, fullpath_mainnews_file)
        )
        DB.con.commit()

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

        file_name = res_link # имя файла
        fullpath_othnews_file = os.path.join(fullpath_othnews,
                                             file_name)  # объеденинение для описания пути к создающемуся файлу
        my_file = open(fullpath_othnews_file + ".txt", "w+")  # открыть файл для записи

        my_file.write(link.text)  # запись названия в файл
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
            o=o+1




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
        DB.cur.execute(
            "INSERT INTO OTHNEWS (NAME,FILE,KATEGORY,COMMENTS) VALUES (%s, %s, %s, %s)", (name_of_f, fullpath_othnews_file, theme, comments)
        )
        DB.con.commit()

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
        my_file.write(news_time)
        news_page = requests.get(news_link)  # для парсинга страницы самой новости
        news = BeautifulSoup(news_page.text, 'html.parser')
        b_all = news.find(name='div', class_='text newtext')  # теги для поиска текста
        for b in b_all:  # текст новости
            if b.find('b') is not None:
                my_file.write(b.text)
            if b.find('p') is not None:
                my_file.write(b.text)
            o=o+1

        DB.cur.execute(
            "INSERT INTO HOURNEWS (NAME,FILE) VALUES (%s, %s)", (link.text, fullpath_hourall_file)
        )
        DB.con.commit()


        news_page = None
        news_link = None

        my_file.close()

# DB.cur.execute("SELECT name, file from HOURNEWS")
# rows = DB.cur.fetchall()
# for row in rows:
#     print("NAME =", row[0])
#     print("FILE =", row[1], "\n")
# DB.cur.execute("SELECT name, file from MAINNEWS")
# rows = DB.cur.fetchall()
# for row in rows:
#     print("NAME =", row[0])
#     print("FILE =", row[1], "\n")
# DB.cur.execute("SELECT name, file from TOPNEWS")
# rows = DB.cur.fetchall()
# for row in rows:
#     print("NAME =", row[0])
#     print("FILE =", row[1], "\n")
# DB.cur.execute("SELECT name, file, kategory, comments from OTHNEWS")
# rows = DB.cur.fetchall()
# for row in rows:
#     print("NAME =", row[0])
#     print("FILE =", row[1])
#     print("KATEGORY =", row[2])
#     print("COMMENTS =", row[3], "\n")
DB.con.close()