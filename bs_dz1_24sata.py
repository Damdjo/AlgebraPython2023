import os
import requests
from bs4 import BeautifulSoup

os.system('cls' if os.name == 'nt' else 'clear')

url_crna_kronika = "https://www.24sata.hr/crna-kronika-news"



response = requests.get(url_crna_kronika)
html_content = response.content


soup = BeautifulSoup(html_content, "html.parser")
cards = soup.find_all("div", class_="card")


for card in cards[:7]:
    #glavni_naslov_element = card.find("span", class_="card__label")
    title_element = card.find("h2", class_="title")
    opis_element= card.find("p")
    if title_element:
        #gl_naslov = glavni_naslov_element.text.strip()
        title = title_element.text.strip()
        opis = opis_element.text.strip()
        
        print(f'{title}\n{opis}\n')
