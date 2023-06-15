#proširiti program koji preuzima prognozu sa neta
#potencijalno imati bazu gradova
#isto tako probati neki meni ukomponirati
#pokušati koristiti requests umjesto urllib


import requests, json, datetime, os



try:
    with open(f"m3/Zadace/zadaca05/meteo_baza_gradova.json", "r") as fr:
        city_dict = json.load(fr)

except Exception as e:
    print(f"Greška {e}") 

def download_city_meteo_data_json(city_name:str):
    """
    program prvo koristeći funkciju check_file_date provjerava jesu li datumi isti/postoje li spreljeni fileovi\n
    ako su isti onda učitava iz spremljenog filea\n
    ako nisu isti onda downloada novi i sprema ga
    
    """    
    if check_file_date(city_name) != True:
        URL = f"https://api.tutiempo.net/json/?lan=en&apid=zwDX4azaz4X4Xqs&ll={city_dict[city_name]}"
        loaded_file = requests.get(URL)
        dict_json_stranica = json.loads(loaded_file.text)
        try:
            city_name = city_name.lower()
            with open(f"m3/Zadace/zadaca05/meteo_data/meteo_{city_name}.json", "w") as fw:
                json.dump(dict_json_stranica,fw, indent=4)
                return dict_json_stranica
        except Exception as e:
            print(f"Greška: {e}")
        
    else:
        try:
            with open(f"m3/Zadace/zadaca05/meteo_data/meteo_{city_name.lower()}.json", "r") as fr:
                dict_json_stranica = json.load(fr)
                return dict_json_stranica              
        except Exception as e:
            print(f"Greška {e}")  

def check_file_date(city_name:str):
    """
    uspoređuje današnji datum sa datumom iz već spremljenog filea\n
    ako podatci nisu isti ili datoteka ne postoji vraća False\n
    ako su isti vraća True

    """
    danas = datetime.date.today()
    danas = danas.strftime("%Y-%m-%d")
    try:
        with open(f"m3/Zadace/zadaca05/meteo_data/meteo_{city_name.lower()}.json", "r") as fr:
            dict_check_data = json.load(fr)
            dict_day1 = dict_check_data["day1"]['date']
            dict_day1 = datetime.datetime.strptime(dict_day1,"%Y-%m-%d")
            dict_day1 = datetime.date.strftime(dict_day1,"%Y-%m-%d")
        if danas == dict_day1:
            return True
        else:
            return False
    except FileNotFoundError:
        #ovo se izvrši ako program ne može naći datoteku za uneseni grad
        return False
    except Exception as e:
        print(f"Greška {e}")
                    


def printaj_dan(dictionary,dan):
    print("*"*55)
    dan = "day"+str(dan)
    print(f"Vremenska prognoza za {dictionary['locality']['name']} na dan {dictionary[dan]['date']}")
    print("\n")
    print(f"\tMinimalna temperatura: {dictionary[dan]['temperature_min']} °C")
    print(f"\tMaximalna temperatura: {dictionary[dan]['temperature_max']} °C")
    print()
    print(f"\tVlaga: {dictionary[dan]['humidity']} %")
    print(f"\tOblačnost: {dictionary[dan]['text']}")
    print(f"\tBrzina vjetra: {dictionary[dan]['wind']} km/h")
    print()

def printaj_sat(dictionary,sat):
    print("*"*55)
    sat = "hour"+str(sat)
    print(f"Vremenska prognoza za {dictionary['locality']['name']} na dan {dictionary['hour_hour'][sat]['date']} u {dictionary['hour_hour'][sat]['hour_data']}")
    print("\n")
    print(f"\tTemperatura: {dictionary['hour_hour'][sat]['temperature']} °C")
    print()
    print(f"\tVlaga: {dictionary['hour_hour'][sat]['humidity']} %")
    print(f"\tTlak: {dictionary['hour_hour'][sat]['pressure']} hPa")
    print()

def print_prognoza(rijecnik_dict):
    for sat in range(3):
        printaj_sat(rijecnik_dict,sat+1)
    for dan in range(1,3):
        printaj_dan(rijecnik_dict,dan+1)

def meni():
    os.system("cls")
    print("*"*50)
    print("Vremenska prognoza".center(50))
    print("\n")
    print("Odaberite jedan od gradova za koji želite prognozu!\n")

    for broj,grad in enumerate(city_dict.keys()):
        print(f"\t{broj+1}. {grad}")
    print()
    while True:
        unos = input("Vaš odabir: ")
        try:
            unos = int(unos)
        except ValueError:
            print(f"Unos mora biti broj!")
        except Exception as e:
            print(f"Greška {e}")
        else:
            break
    match unos:
        case 1:
            meteo_dict = download_city_meteo_data_json("Karlovac")
            print_prognoza(meteo_dict)
            
        case 2:
            meteo_dict = download_city_meteo_data_json("Zagreb")
            print_prognoza(meteo_dict)
            
        case 3:
            meteo_dict = download_city_meteo_data_json("Split")
            print_prognoza(meteo_dict)
            
        case 4:
            meteo_dict = download_city_meteo_data_json("Zadar")
            print_prognoza(meteo_dict)
            
        case 5:
            meteo_dict = download_city_meteo_data_json("Dubrovnik")
            print_prognoza(meteo_dict)

        
            
            
        
            





def main(): 
   
    meni()

main()