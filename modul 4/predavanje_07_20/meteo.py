from sense_emu import SenseHat
from time import sleep
sense = SenseHat()

temperature = sense.get_temperature()
temp_from_hum = sense.get_temperature_from_humidity()
temp_from_pre = sense.get_temperature_from_pressure()


print(temperature)
print(temp_from_hum)
print(temp_from_pre)

tlak = sense.get_pressure()
print(tlak)

vlaga = sense.get_humidity()
print(vlaga)

"""
for t in range(1):
    temperature = sense.get_temperature()
    print(temperature)
    sleep(1)
"""

tempe = round(sense.get_temperature(),2)
tlak = round(sense.get_pressure(),1)
vlaga = round(sense.get_humidity(),1)

ispis = f"Temp: {tempe}; Tlak: {tlak}; Vlaga: {vlaga}"
sense.show_message(ispis)