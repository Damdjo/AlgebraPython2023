import json

povuceno = {}


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





try:
    with open("m3/datoteke/meteo.json", "r") as fr:
        povuceno = json.load(fr)
except Exception as e:
    print(f"Greška: {e}")
"""
try:
    with open("m3/datoteke/meteo.json", "w") as fw:
        json.dump(povuceno,fw, indent=4)
except Exception as e:
    print(f"Greška: {e}")
"""


#ispisujemo vremensku prognozu za sljedecih 3 dana, a za današnji dan prognozu za sljedeća 3 sata
#podatci: temp_min, temp_max, vlaga, oblacnost, vjetar
#podatci za sate: temp, vlaga i tlak



for sat in range(3):
    printaj_sat(povuceno,sat+1)
for dan in range(1,3):
    printaj_dan(povuceno,dan+1)
