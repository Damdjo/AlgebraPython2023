from PIL import Image, ImageEnhance
import os
os.chdir("m3/datoteke/pillow/")

img = Image.open("slike/Algebra_campus.jpg")

#img_enh1 = ImageEnhance.Brightness(img)
#img_enh1.enhance(4).show()

#img_enh2 = ImageEnhance.Contrast(img)
#img_enh2.enhance(4).show()

#img_enh3 = ImageEnhance.Sharpness(img)
#img_enh3.enhance(4).show()

img_enh4 = ImageEnhance.Color(img)
img_enh4.enhance(4).show()