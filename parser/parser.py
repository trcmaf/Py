from bs4 import BeautifulSoup
import requests
from parser.final import tkinter as tk

window = tk.Tk()

url = 'http://vz.ru'
page = requests.get(url)
print (page.status_code) # статус код = 200 --> подключено
filtered_news = []
all_news = []
all = []
soup = BeautifulSoup(page.text, "html.parser")
print (soup)
all = soup.findAll('div', class_='text')

for i in all:
    all_news.append(str(i))
N = len(all_news)
for y in range(N):
    print(all_news[y])

"""for data in all_news:
    if data.find('strong', class_='material-type') is not None:
    #if data.find('a', string='economy') is not None:    #if data.find('strong', class_='material-type') is not None:
        filtered_news.append(data.text)

for data in filtered_news:
    print (data)"""