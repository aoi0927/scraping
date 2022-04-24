from bs4 import BeautifulSoup
import urllib.request
import csv

print('スクレイピングしたいurlを入力')
url = input('>> ')
html = urllib.request.urlopen(url).read().decode('UTF-8')  
soup= BeautifulSoup(html, "lxml")

data = soup.find_all('tr', {'class':'ek-hour_line'})

station = soup.find('div', {'class': 'station-name'}).text.split()[0][:-1]

for i in data:
    hour = i.find('td')
    print(hour)
    min = i.find_all('span', {'class': 'time-min means-text'})
    min2 = i.find_all('span', {'class': 'time-min means-text start'})
    min.extend(min2)
    detail_data = i.find_all('li', {'class':'ek-tooltip ek-narrow ek-train-tooltip'})
    for j, m in enumerate(min):
        print(f'{hour.text}:{m.text} {detail_data[j]["data-tr-type"]} {detail_data[j]["data-dest"]}行き')