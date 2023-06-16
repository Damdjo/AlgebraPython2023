import requests
from bs4 import BeautifulSoup

URL_COVID = "https://www.worldometers.info/coronavirus"

covid_stranica = BeautifulSoup(requests.get(URL_COVID).content, "html.parser")

svi_podatci = covid_stranica.find_all("div", id = "maincounter-wrap")
#print(svi_podatci)

covid_slucajeva = svi_podatci[0]
covid_smrti = svi_podatci[1]
covid_oporavljeni = svi_podatci[2]

#print(covid_slucajeva)


for item in svi_podatci:
    naslov = item.find("h1").get_text()
    vrijednost = item.find("span").get_text()
    print(naslov, vrijednost)