from bs4 import BeautifulSoup
import urllib.request

url = 'https://ekitan.com/timetable/railway/line-station/193-0/d1'
html = urllib.request.urlopen(url).read().decode('UTF-8')  
soup= BeautifulSoup(html, "lxml")

tbody = soup.find_all('tr', {'class':'ek-hour_line'})

print(tbody)

for i in tbody:
    hour = i.find('td')
    min = i.find_all('span', {'class': 'time-min means-text'})
    a = i.find_all('li', {'class':'ek-tooltip ek-narrow ek-train-tooltip'})
    for j, m in enumerate(min):
        print(f'{hour.text}:{m.text} {a[j]["data-dest"]} {a[j]["data-tr-type"]}')