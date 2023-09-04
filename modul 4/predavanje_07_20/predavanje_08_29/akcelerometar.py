from sense_emu import SenseHat
from time import sleep
sense = SenseHat()

boje = {
    "white": (255,255,255),
    "red" : (255,0,0),
    "green" : (0,255,0),
    "blue" : (0,0,255),
    "zuta" : (255,200,0),
    "cyan" : (0,255,255),
    "magenta" : (255,0,255),
    "orange" : (255,122,56),
    "tan" : (200,255,134)
    }
pos_roll = [0,4]
pos_pitch = [0,2]
pos_yaw = [0,0]

delay = 0.5


while True:
    
    #yaw,pitch,roll
    roll,pitch,yaw = sense.get_orientation().values()

    pitch = round(pitch,0)
    yaw = round(yaw,0)
    roll = round(roll,0)
    #ROLL
    if roll > 0 and roll < 180:
        pos_roll[0]+=1
        if pos_roll[0]==8:
            pos_roll[0] = 7        
            if roll>90:
                sleep(delay/2)
            else:
                sleep(delay)
    elif roll > 180 and roll < 360:
        pos_roll[0]-=1
        if pos_roll[0]==-1:
            pos_roll[0] = 0
            if roll<270:
                sleep(delay/2)
            else:
                sleep(delay)
    else:
        pass
    
    #PITCH
    if pitch > 0 and pitch < 180:
        pos_pitch[0]+=1
        if pos_pitch[0]==8:
            pos_pitch[0] = 7        
            if roll>90:
                sleep(delay/2)
            else:
                sleep(delay)
    elif pitch > 180 and pitch < 360:
        pos_pitch[0]-=1
        if pos_pitch[0]==-1:
            pos_pitch[0] = 0
            if pitch<270:
                sleep(delay/2)
            else:
                sleep(delay)
    else:
        pass
    
    #YAW
    if yaw > 0 and yaw < 180:
        pos_yaw[0]+=1
        if pos_yaw[0]==8:
            pos_yaw[0] = 7        
            if yaw>90:
                sleep(delay/2)
            else:
                sleep(delay)
    elif yaw > 180 and yaw < 360:
        pos_yaw[0]-=1
        if pos_yaw[0]==-1:
            pos_yaw[0] = 0
            if yaw<270:
                sleep(delay/2)
            else:
                sleep(delay)
    else:
        pass
                
    sense.clear()            
    sense.set_pixel(pos_yaw[0],pos_yaw[1],boje["red"])
    sense.set_pixel(pos_pitch[0],pos_pitch[1],boje["green"])
    sense.set_pixel(pos_roll[0],pos_roll[1],boje["blue"])
    
    
    sleep(delay)
    print(yaw,pitch,roll)
    
