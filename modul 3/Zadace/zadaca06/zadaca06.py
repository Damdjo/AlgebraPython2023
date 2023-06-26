


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

def write(input_data, filename,folder=""):
    data_to_write = input_data
    try:            
        with open(f"m3/Zadace/zadaca06/site_data/{folder}{filename}.json", "w", encoding="utf-8") as fw:
            json.dump(data_to_write,fw, indent=4, ensure_ascii=False)
            return data_to_write
    except Exception as e:
        print(f"Greška: {e}")

def pull_data(URL, kategorija):
    data_dict = {}
    stranica_kategorija = BeautifulSoup(requests.get(URL).content, "html.parser")
    proizvodi = stranica_kategorija.find_all("div", class_ = "col-lg-3 col-md-4 col-6 col-sm-6 product-item-box grid productEntity")
    for proizvod in proizvodi:

        proizvod_id = proizvod.find("div", class_ = "product-list-sifra-artikla").text.strip()
       
        #slice da se makne dostupnost iz sifre artikla        
        proizvod_id = proizvod_id[0:11:1]

        proizvod_dostupnost = proizvod.find("div", class_ = "product-list-sifra-artikla").text.strip()
        proizvod_dostupnost = proizvod_dostupnost[13::1]        
        
        
        proizvod_naziv = proizvod.find("h2", class_ = "title").text.strip()

        proizvod_cijena = proizvod.find("div", class_ = "price d-flex flex-column").text.strip()        
        kn_index = proizvod_cijena.find("Kn")
        kn = proizvod_cijena[0:kn_index+2:1]
        eur = proizvod_cijena[kn_index+3::1]

        data_dict[proizvod_id] = {"sifra artikla":proizvod_id,"dostupnost":proizvod_dostupnost,"naziv":proizvod_naziv, "cijena €":eur, "cijena Kn":kn,}
    write(data_dict,f"{kategorija}_data",f"podatci/")
      
    """try:
        with open(f"m3/Zadace/zadaca05/meteo_data/meteo_{city_name}.json", "w") as fw:
            json.dump(dict_json_stranica,fw, indent=4)
            return dict_json_stranica
    except Exception as e:
        print(f"Greška: {e}") """          
            
            
        #print(f"*{proizvod_cijena}*")
    

#Povlačenje kategorija iz menija
def pull_kategorije():
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







def main():

    pull_kategorije()
    kategorije_dict = {}
    try:
        with open(f"m3/Zadace/zadaca06/site_data/kategorije.json", "r") as fr:
            kategorije_dict = json.load(fr)              
    except Exception as e:
        print(f"Greška {e}")  

    for key,value in kategorije_dict.items():    
        URL_kategorija = f"{URL}{value}/{key}/l/{products_per_page_suffix}"
        pull_data(URL_kategorija,value)
        print(f"{value} done!") 




main()



