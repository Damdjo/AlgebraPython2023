from PIL import Image

fotografija_putanja = r"m3/datoteke/pillow/slike/Algebra_campus.jpg"
fotografije_varijabla = Image.open(fotografija_putanja)

print(fotografije_varijabla.size)

smanji_za = 500
lijevo = 0+smanji_za
gore = 0+smanji_za
desno = fotografije_varijabla.size[0] - smanji_za
dolje = fotografije_varijabla.size[1] - smanji_za

fotografije_varijabla_crop = fotografije_varijabla.crop((lijevo,gore,desno,dolje))

fotografije_varijabla.show()
fotografije_varijabla_crop.show()

fotografije_varijabla_crop.save("Algebra_campus_crop.jpg", "JPEG")
fotografije_varijabla_crop.save("Algebra_campus_crop.png", "PNG")