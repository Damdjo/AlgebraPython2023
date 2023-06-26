from PIL import Image

#ovo je za promjenu gdje se terminal otvara
import os

os.chdir("m3/datoteke/pillow/")
#NIJE RELEVANTNO ZA PREDAVANJE

fotografija_putanja = r"slike/Algebra_campus.jpg"
fotografije_varijabla = Image.open(fotografija_putanja)

fotografija_preko = Image.open(r"slike/Python_logo_and_wordmark.png")

print(fotografija_preko.size)
print(fotografije_varijabla.size)

fotografije_varijabla.paste(fotografija_preko,(500,500))
fotografije_varijabla.show()