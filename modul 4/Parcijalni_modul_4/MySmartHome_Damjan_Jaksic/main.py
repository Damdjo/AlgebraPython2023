#nas meteo dio
from Meteo import meteo
from database import db_main

from sense_emu import SenseHat
from time import sleep
import tkinter as tk
from tkinter import ttk
import threading

data = meteo.get_meteo_data()
t_data = meteo.timed_data(data)
lokacija = "Karlovac"
sense = SenseHat()
indoor_meteo_data = (None,None,None)
outdoor_meteo_data = (None,None,None,None)

#print(t_data[-1])

def get_sense_temp():
    temp = round(sense.get_temperature(),1)
    tlak = round(sense.get_pressure(),1)
    vlaga = int(round(sense.get_humidity(),0))
    return(temp,tlak,vlaga)

def temp_by_location(location:str,meteo_data:list):
    global outdoor_meteo_data
    data = meteo.timed_data(meteo_data)
    
    for grad in data:
        if grad[0] == location:            
            db_main.insert_sensor_data("outdoor", grad[1], grad[2], grad[3])
            outdoor_meteo_data = grad
            return grad
        
def update_strVar(strvar1, strvar2):
    global indoor_meteo_data
    indoor_meteo_data = get_sense_temp() 
    strvar1.set(indoor_meteo_data[0])    
    strvar2.set(indoor_meteo_data[2])            
    db_main.insert_sensor_data("indoor", indoor_meteo_data[0], indoor_meteo_data[1], indoor_meteo_data[2])
    print(indoor_meteo_data)

def set_icon(temp):
    sleep(0.5)
    temp = float(temp)
    if temp > 22:
        return "kratki rukavi"
    elif temp <= 22 and temp > 12:
        return "lagana jakna"
    elif temp <= 12 and temp >0:
        return "zimska jakna"
    else:
        return "kapa, šal i zimska jakna"

    
def main():
    global indoor_meteo_data
    
    selected = 0
    boje = {
        "red" : (255,0,0),
        "green" : (0,255,0),
        "blue" : (0,0,255),
        "zuta" : (255,200,0),
        "cyan" : (0,255,255),
        "magenta" : (255,0,255),
        "orange" : (255,122,56),
        "tan" : (200,255,134),
        "brown" : (139,69,19)
        }   
    
    sense.clear()
    
    
    while True:
        
        
        for event in sense.stick.get_events():
            if event.action == "pressed":
                ####GORE
                if event.direction == "up":
                    pass
            
                ###DOLJE    
                if event.direction == "down":
                    pass
                    
                elif event.direction == "left":
                    pass
                    
                elif event.direction == "right":
                    pass
                    
                elif event.direction == "middle":
                    pass
        """ 
        if indoor_meteo_data != new:
            indoor_meteo_data = new
            update_strVar()
            
            
            print("test")
        """
                
        #print("Inside: ",indoor_data)        
        #print("Outside: ",temp_by_location(lokacija, t_data))
        
            
        sleep(0.25)
        
        
def main_gui():
    global indoor_meteo_data
    #dio za GUI
    root = tk.Tk()

    root.title("MySmartHome")
    root.geometry("800x400")
    tabMain = ttk.Notebook(root)
    
    tabMeteo = ttk.Frame(tabMain)
    tabBaza = ttk.Frame(tabMain)
    
    
    
    tabMain.add(tabMeteo, text = "Meteo")
    tabMain.add(tabBaza, text = "Baza")
    tabMain.grid()
    
    
    #tabBaza
    bazaFrame = tk.Frame(tabBaza, width = 800, height = 390) 
    bazaFrame.grid(row = 0,column = 0, columnspan = 3, sticky = "NSEW")
    
    showButton = tk.Button(bazaFrame, text = "Print data into console",command = lambda :db_main.show_data())
    showButton.grid(row = 0,column = 0, sticky = "NSEW")
    
    
    #tabMeteo
    meteoFrame = tk.Frame(tabMeteo, width = 800, height = 390) 
    meteoFrame.grid(row = 0,column = 0, columnspan = 3, sticky = "NSEW")
    
    #outdoor
    outdoor = tk.Frame(meteoFrame, width = 250, height = 390, pady = 20) 
    outdoor.grid(row = 0,column = 0, columnspan = 1, rowspan = 6)
    
    outdoorTempLabel = tk.Label(outdoor, text = "OUTDOOR TEMPERATURE")
    outdoorTempLabel.grid(row = 0, column = 0, sticky = "N")
    
    outdoorTempVar = tk.StringVar()
    outdoorTempVar.set(outdoor_meteo_data[1])
    outdoorTemp = tk.Label(outdoor, textvar = outdoorTempVar, font = ("",60))
    outdoorTemp.grid(row = 1, column = 0, sticky = "N")
    
    outdoorHumLabel = tk.Label(outdoor, text = "HUMIDITY")
    outdoorHumLabel.grid(row = 2, column = 0, sticky = "N")
    
    outdoorHumVar = tk.StringVar()
    outdoorHumVar.set(outdoor_meteo_data[2])
    outdoorHum = tk.Label(outdoor, textvar = outdoorHumVar, font = ("",60))
    outdoorHum.grid(row = 3, column = 0, sticky = "N")
    
    #data
    dataFrame = tk.Frame(meteoFrame, width = 300, height = 390, padx = 30, pady = 20) 
    dataFrame.grid(row = 0, rowspan = 3, column = 1, columnspan = 1)
    dataFrame.rowconfigure(0, weight = 10)    
    dataFrame.rowconfigure((1,2), weight = 0)
    
    dataIconVar = tk.StringVar()
    ikonica = set_icon(outdoor_meteo_data[1])
    dataIconVar.set(ikonica)
    dataIcon = tk.Label(dataFrame, textvar = dataIconVar, padx = 30, pady = 20)
    dataIcon.grid(row = 0, column = 0, sticky = "NEW")
    
    dataPresLabel = tk.Label(dataFrame, text = "PRESSURE")
    dataPresLabel.grid(row = 1, column = 0, sticky = "S")
    
    dataPresVar = tk.StringVar()
    dataPresVar.set(outdoor_meteo_data[3])
    dataPres = tk.Label(dataFrame, textvar = dataPresVar, font = ("",50))
    dataPres.grid(row = 2,rowspan = 2, column = 0, sticky = "SEW")
    
    
    
    #indoor
    indoor = tk.Frame(meteoFrame, width = 250, height = 390, padx = 30, pady = 20) 
    indoor.grid(row = 0,column = 2, columnspan = 1)
    
    indoorTempLabel = tk.Label(indoor, text = "INDOOR TEMPERATURE")
    indoorTempLabel.grid(row = 0, column = 0, sticky = "N")
    
    indoorTempVar = tk.StringVar()
    indoorTempVar.set(indoor_meteo_data[0])
    indoorTemp = tk.Label(indoor, textvar = indoorTempVar, font = ("",60))
    indoorTemp.grid(row = 1, column = 0, sticky = "N")
    
    indoorHumLabel = tk.Label(indoor, text = "HUMIDITY")
    indoorHumLabel.grid(row = 2, column = 0, sticky = "N")
    
    indoorHumVar = tk.StringVar()
    indoorHumVar.set(indoor_meteo_data[2])
    indoorHum = tk.Label(indoor, textvar = indoorHumVar, font = ("",60))
    indoorHum.grid(row = 3, column = 0, sticky = "N")
    
    
    
    

    #glavna petlja
    meteoFrame.bind("<Visibility>", func = lambda x:update_strVar(indoorTempVar,indoorHumVar))
    root.mainloop()
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
indoor_meteo_data = get_sense_temp()
outdoor_meteo_data = temp_by_location(lokacija, t_data)    
    
t1 = threading.Thread(target = main, group = None).start()
t2 = threading.Thread(target = main_gui, group = None).start()  
    
    
