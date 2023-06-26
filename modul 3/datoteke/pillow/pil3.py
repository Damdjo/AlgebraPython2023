from PIL import Image

#ovo je za promjenu gdje se terminal otvara
import os

os.chdir("m3/datoteke/pillow/")
#nije relevantno za predavanje

fotografija_putanja = r"slike/Algebra_campus.jpg"
fotografije_varijabla = Image.open(fotografija_putanja)

print(fotografije_varijabla.mode)

fotografije_varijabla_convert = fotografije_varijabla.convert(mode = "L")
fotografije_varijabla_convert.show()
fotografije_varijabla_convert.save("slike/Algebra_campus.jpg", "JPEG")
print(fotografije_varijabla_convert.mode)