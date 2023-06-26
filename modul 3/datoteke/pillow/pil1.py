from PIL import Image

fotografija_putanja = r"m3/datoteke/pillow/slike/Algebra_campus.jpg"
fotografije_varijabla = Image.open(fotografija_putanja)

print(fotografije_varijabla)
#format
print(f"format slike: {fotografije_varijabla.format}")
print(f"mode slike: {fotografije_varijabla.mode}")
print(f"dimenzije slike: {fotografije_varijabla.size}")

fotografije_varijabla.show()