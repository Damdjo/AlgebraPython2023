import os
import requests
from bs4 import BeautifulSoup

os.system('cls' if os.name == 'nt' else 'clear')

def meni():
    print('-'*40)
    print('*'*10, 'KATEGORIJE', '*'*10)
    print('-'*40)
    print('\t1. Crna kronika\t')
    print('\t2. Hrvatska\t')
    print('\t3. Svijet\t')
    print('\t4. Politika\t')
    print('-'*40)

url_crna_kronika = "https://www.24sata.hr/crna-kronika-news"
url_hrvatska = "https://www.24sata.hr/hrvatska"
url_svijet = "https://www.24sata.hr/svijet"
url_politika = "https://www.24sata.hr/politika"

def vijesti(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")
    cards = soup.find_all("div", class_="card")

    for card in cards[:7]:
        title_element = card.find("h2", class_="title")
        opis_element = card.find("p")
        if title_element:
            title = title_element.text.strip()
            opis = opis_element.text.strip()
            print(f'{title}\n{opis}\n')

while True:
    meni()
    odabir = input("Odaberite kategoriju (1-4) ili 'q' za izlaz: \n")

    if odabir == 'q':
        break
    elif odabir == '1':
        print("Crna kronika:\n")
        vijesti(url_crna_kronika)
    elif odabir == '2':
        print("Hrvatska:\n")
        vijesti(url_hrvatska)
    elif odabir == '3':
        print("Svijet:\n")
        vijesti(url_svijet)
    elif odabir == '4':
        print("Politika:\n")
        vijesti(url_politika)
    else:
        print("Pogrešan unos. Molimo unesite broj od 1 do 4 ili 'q' za izlaz.")
