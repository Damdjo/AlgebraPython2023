import cv2
import os
os.chdir("m3/datoteke/opencv/") #Ovdje mijenjam direktorij

face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
foto = cv2.imread("slike/Algebra_greyp.jpg")
cb_foto = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

prepoznata_lica = face_cascade.detectMultiScale(
    cb_foto,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (30,30)
)

print(f"Pronađeno je {len(prepoznata_lica)} lica")

for (x, y, w ,h) in prepoznata_lica:
    cv2.rectangle(foto, (x, y, w, h), (0,255,0),2)

cv2.imshow("Pronadjena lica",foto)

cv2.waitKey()