from PIL import Image, ImageDraw
import os
os.chdir("m3/datoteke/pillow/")

img = Image.open("slike/Algebra_campus.jpg")
img_draw = ImageDraw.Draw(img)

img_draw.rectangle((800,500,3400,2200), fill=None, outline="red", width=10)
#img.show()

img_draw.ellipse((800,500,3400,2200), fill="blue", outline="red", width=10)
#img.show()

img_draw.line((800,500,3400,2200), fill="#F0B347", width=10)
img.show()