import requests, openpyxl
from bs4 import BeautifulSoup as soup
url = f'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
page = requests.get(url)
page_content = soup(page.text, 'html.parser')
wb = openpyxl.Workbook()
ws = wb.active
ws.title='IMDB'
ws.append(['Rank', 'Name', 'Year','Rating'])

movies =page_content.find('tbody', class_='lister-list').find_all('tr')
for movie in movies:
    name = movie.find('td', class_='titleColumn').a.text
    rank = movie.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]
    year = movie.find('span', class_='secondaryInfo').text.strip('()')
    rating = movie.find('td', class_='ratingColumn').text.strip()
    ws.append([rank, name, year, rating])
    
wb.save('Imdb_file.xlsx')
