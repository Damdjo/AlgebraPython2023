from PIL import Image

#ovo je za promjenu gdje se terminal otvara
import os

os.chdir("m3/datoteke/pillow/")
#NIJE RELEVANTNO ZA PREDAVANJE

fotografija_putanja = r"slike/Algebra_campus.jpg"
fotografija = Image.open(fotografija_putanja)

#fotografija_trans_TB = fotografija.transpose(Image.FLIP_TOP_BOTTOM).show()
#fotografija_trans_LR = fotografija.transpose(Image.FLIP_LEFT_RIGHT).show()
#fotografija_trans_R90 = fotografija.transpose(Image.ROTATE_90).show()
#fotografija_trans_R180 = fotografija.transpose(Image.ROTATE_180).show()
#fotografija_trans_R270 = fotografija.transpose(Image.ROTATE_270).show()
#fotografija_trans_TS = fotografija.transpose(Image.TRANSPOSE).show()
fotografija_trans_TV = fotografija.transpose(Image.TRANSVERSE).show()