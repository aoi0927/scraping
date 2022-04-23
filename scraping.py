from bs4 import BeautifulSoup
import urllib.request

print('スクレイピングしたいurlを入力')
url = input('>> ')
html = urllib.request.urlopen(url).read().decode('UTF-8')  
soup= BeautifulSoup(html, "lxml")

tbody = soup.find_all('tr', {'class':'ek-hour_line'})

for i in tbody:
    hour = i.find('td')
    min = i.find_all('span', {'class': 'time-min means-text'})
    a = i.find_all('li', {'class':'ek-tooltip ek-narrow ek-train-tooltip'})
    for j, m in enumerate(min):
        print(f'{hour.text}:{m.text} {a[j]["data-tr-type"]} {a[j]["data-dest"]}行き')