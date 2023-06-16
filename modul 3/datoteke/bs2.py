import requests
from bs4 import BeautifulSoup

def get_ocjena(tag):
    for naziv, broj_zvjezdica in opis_ocjena.items():
        if naziv in tag["class"]:
            return broj_zvjezdica
        
opis_ocjena = {
    "One" : "*",
    "Two" : "* *",
    "Three" : "* * *",
    "Four" : "* * * *",
    "Five" : "* * * * * ",
}




cijena_selector = ".price_color"
naslov_selector = ".product_pod h3 a"
ocjena_selector = ".star-rating"

sirovi_podatci = requests.get("http://books.toscrape.com/").content
sadrzaj = BeautifulSoup(sirovi_podatci, "html.parser")

cijene = sadrzaj.select(cijena_selector)
naslovi = sadrzaj.select(naslov_selector)
ocjene = sadrzaj.select(ocjena_selector)

for cijena, naslov, ocjena in zip(cijene, naslovi, ocjene):
    print(f"{naslov['title']};{cijena.string};{get_ocjena(ocjena)} ")