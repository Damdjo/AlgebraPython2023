


#Pronaći neku stranicu koja nam može koristiti (njuškalo, vrijeme, crna kronika,...)
#probati povući podatke sa navedene stranice

# OPCIONALNO - ako je zanimljivo
# https://github.com/public-apis/public-apis - popis javno dostupnih API-eva
# Stranice koje ne traže AUTH niti APIKEY
# Anti je zanimljiv networkcalc
# dohvatiti JSON i uobličiti ga

import requests, json, datetime, os
from bs4 import BeautifulSoup

URL = "https://www.adm.hr/"
products_per_page_suffix = "?p=1&s=1000"

stranica = BeautifulSoup(requests.get(URL).content, "html.parser")




#micanje posebnih znakova iz kategorija kako bi linkovi radili
def text_format(string):
    parsed = string    
    parsed = parsed.replace("ž","z")
    parsed = parsed.replace("š","s")
    parsed = parsed.replace("đ","d")
    parsed = parsed.replace("č","c")
    parsed = parsed.replace("ć","c")
    parsed = parsed.replace(" ","-")    
    parsed = parsed.replace(",","")            
    return parsed.lower()

def write(input_data, filename):
    data_to_write = input_data
    try:            
        with open(f"m3/Zadace/zadaca06/site_data/{filename}.json", "w") as fw:
            json.dump(data_to_write,fw, indent=4)
            return data_to_write
    except Exception as e:
        print(f"Greška: {e}")



#Povlačenje kategorija iz menija
kategorije_dict = {}
kategorije = stranica.find_all("li", class_ = "yamm-fw menu-item menu-item-has-children animate-dropdown dropdown-submenu d-flex h-100")
for broj, kategorija in enumerate(kategorije):
    main_kategorija = kategorija.find("a", class_ = "justify-content-center align-self-center dropdown-toggle")
    text_kategorija = text_format(main_kategorija.text.strip())
    match text_kategorija:
        case "proizvodi-umanjene-vrijednosti":
            kategorije_dict[17] = text_kategorija
        case _:
            kategorije_dict[broj+1] = text_kategorija

print()
write(kategorije_dict,"kategorije")

#URL_kategorija = f""

for key,value in kategorije_dict.items():
    
    URL_kategorija = f"{URL}{value}/{key}/l/{products_per_page_suffix}"
    print(URL_kategorija)
stranica_kategorija = BeautifulSoup(requests.get(URL).content, "html.parser")