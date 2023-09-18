import datetime as dt
import requests
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://vrijeme.hr/hrvatska_n.xml"


def get_meteo_data():
    response=requests.get(url).content
    data = BeautifulSoup(response, "html.parser")

    gradovi = data.select("gradime")
    temperature = data.select("temp")
    vlage = data.select("vlaga")
    tlakovi = data.select("tlak")

    parsed_list = []

    for index in range(len(gradovi)):
        grad = gradovi[index]
        temp = temperature[index]
        vlaga = vlage[index]
        tlak = tlakovi[index]
        parsed_list.append((grad.text,temp.text,vlaga.text,tlak.text))
    
    last_update = dt.datetime.now()
    parsed_list.append(last_update)
    return parsed_list


def timed_data(lista_gradova):
    
    temp_last_updated = lista_gradova[-1].minute
    old = lista_gradova[0:-1]
    old_lu = lista_gradova[-1]
    test = temp_last_updated//15*15%60
    lista_gradova[-1] = lista_gradova[-1].replace(minute = test)
    
    if temp_last_updated < test or test == 0:
        lista_gradova[-1] = dt.datetime.now()
        temp_gradovi = get_meteo_data()
        timed_popis_gradova = lista_gradova
        #print(lista_gradova[-1], "if", test)
        return timed_popis_gradova
    else:
        #print(lista_gradova[-1],"else", test)
        lista_gradova[-1] = old_lu
        timed_popis_gradova = lista_gradova
        return timed_popis_gradova
    

def main():
    data_gradovi = get_meteo_data()
    test = timed_data(data_gradovi)
    print(test)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()

    
