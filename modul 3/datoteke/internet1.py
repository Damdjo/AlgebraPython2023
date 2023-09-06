import urllib.request
import urllib.parse
import json

URL = "https://www.algebra.hr"
URL2 = "https://api.tutiempo.net/json/?lan=en&apid=zwDX4azaz4X4Xqs&ll=45.7,15.554916"
connection = urllib.request.urlopen(URL2)

stranica = connection.read().decode()
dict_json_stranica = json.loads(stranica)





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

for sat in range(3):
    printaj_sat(dict_json_stranica,sat+1)
for dan in range(1,3):
    printaj_dan(dict_json_stranica,dan+1)