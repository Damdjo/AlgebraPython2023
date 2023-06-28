import cv2, numpy
import os
os.chdir("m3/datoteke/opencv/") #Ovdje mijenjam direktorij

if not os.path.exists("Rezultat"):
    os.makedirs("Rezultat")

foto = "slike/Algebra_greyp.jpg"

model = cv2.dnn.readNetFromCaffe("deepML/deploy.prototxt","deepML/weights.caffemodel")

foto_cv2 = cv2.imread(foto)

(height, width) = foto_cv2.shape[:2]

blob_image = cv2.dnn.blobFromImage(cv2.resize(foto_cv2, (300,300)), 1.0, (300,300), (104.0, 177.0, 123.0))

model.setInput(blob_image)

detektirana_lica = model.forward()

broj_lica = 0
for i in range(0,detektirana_lica.shape[2]):
    okvir = detektirana_lica[0,0,i, 3:7]*numpy.array([width, height, width, height])
    (startx, starty, endx, endy) = okvir.astype("int")

    vjerojatnost = detektirana_lica[0, 0, i, 2]
    if vjerojatnost > 0.140:
        cv2.rectangle(foto_cv2, (startx, starty, endx, endy), (0,255,0),2 )
        broj_lica += 1
cv2.imshow("Pronađena lica", foto_cv2)
cv2.waitKey()