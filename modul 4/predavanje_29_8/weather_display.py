from sense_emu import SenseHat
from time import sleep
sense = SenseHat()
boje_kljucevi = ["red","green","blue"]
boje = {
    "red" : (255,0,0),
    "green" : (0,255,0),
    "blue" : (0,0,255)
    }
pos_temp = [0,7]
pos_pressure = [2,7]
pos_humidity = [4,7]

delay = 0.5


while True:
    
    #temp, pressure, humidity
    temp = round(sense.get_temperature(),0)
    pressure = round(sense.get_pressure(),0)
    humidity = round(sense.get_humidity(),0)
    #TEMP
    
    temp_pixel = round((((temp+30) / 19.2857142857)-7)*-1,0)
    pos_temp[1] = int(temp_pixel)
    
    #PRESSURE
    pressure_pixel = round((((pressure-260) / 142.857142857)-7)*-1,0)
    pos_pressure[1] = int(pressure_pixel)
    
    #HUMIDITY
    
    humidity_pixel = round(((humidity / 14.2857142857)-7)*-1,0)
    pos_humidity[1] = int(humidity_pixel)
    
                
    sense.clear()
    for broj_temp in range (7,int(pos_temp[1])-1,-1):
        sense.set_pixel(pos_temp[0],broj_temp,boje["red"])
    
    for broj_pre in range (7,int(pos_pressure[1])-1,-1):
        sense.set_pixel(pos_pressure[0],broj_pre,boje["green"])
    
    for broj_hum in range (7,int(pos_humidity[1])-1,-1):
        sense.set_pixel(pos_humidity[0],broj_hum,boje["blue"])
    
    
    print(temp, pressure, humidity)
    sleep(delay)

