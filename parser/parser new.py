from bs4 import BeautifulSoup
import requests

#window = tk.Tk()

url = 'http://vz.ru'
page = requests.get(url)
print (page.status_code) # статус код = 200 --> подключено
filtered_news = []
all_news = []
soup = BeautifulSoup(page.text, "html.parser")
#print (soup)
#all_news = soup.findAll('div', class_='fixed_wrap2')

"""main_all = soup.findAll('div', class_='mainnews')
main_filtr = []
for data in main_all:
    if data.find('h1') is not None:
        main_filtr.append(data.text)
for data in main_all:
    print (data.text)"""

oth_all = soup.findAll(name='div', class_='othnews') #findAll
oth_filtr = []
for data in oth_all:
    if data.find(name='h4') is not None:
        oth_filtr.append(data.text)
for data in oth_all:
    print (data.text)
#for data in main_filtr:
    #print (data)
#for data in all_news:
   # print (data)


#for data in all_news:
  #  if data.find('span', class_='material-title') is not None:
  #      filtered_news.append(data.text)

#for data in filtered_news:
   # print (data)