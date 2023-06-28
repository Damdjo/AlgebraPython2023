#Napraviti mini photoshop
#Izbornik u kojem će korisnik birati radnje koje će se izvršavati na slici



    
from PIL import Image, ImageFilter
import os
#ovo je za promjenu gdje se terminal otvara
os.chdir("m3/Zadace/zadaca07/")


 
    
def iface(lista:list, izlaz:bool=False, sub:str="") -> None:
    """
    lista -> lista sa popisom opcija koja se printaju jedan ispod druge sa rednim brojevima\n    
    ***od opcija izlaz i login_logout samo jedna može biti aktivna***\n
    ***izlaz -> ako je True onda se na kraju ispiše opcija 0. Izlaz\n
    ***login_logout -> ako je True onda se na kraju ispiše opcija 0. Logout
                    -> možemo proslijediti i argument odjel koji će se ispisazi uz MENI
    """   
    
    
    meni =  sub
    
    
    
    
    meni.upper()
    duzina = int(50/2-len(meni)/2)

    print('*'*50)
    print(' '*duzina,meni,)
    print('*'*50)
    for broj, stavka in enumerate(lista):
        print(f'\t{broj+1}. {stavka}')
    if izlaz :
        print('\n\t0. Izlaz')

main_menu = ["Manipulacije", "Filteri"]
manipulacije_menu = ["Rotate", "Zrcaljenje"]
filteri_menu = ["CONTOUR", "EDGE ENHANCE", "EMBOSS", "FIND EDGES", "SHARPEN", "SMOOTH", "Box Blur","Gaussian blur", "Unsharp Mask", "Median Filter", "Max Filter", "Min Filter"]




fotografija_putanja = r"slike/Algebra_campus.jpg"
foto = Image.open(fotografija_putanja)

def enter_to_continue():
    input("Press enter to continue...")

status = 0
while status != -1:
    iface(main_menu, True, "Main")
    status = input("Unesite odabir: ")
    try: 
        int(status)
    except ValueError: 
        print("Unos mora biti broj!")
        enter_to_continue()
    else:
        status = int(status)
    match status:
        case 0:
            break
        case 1:
            sub_status = 0
            while sub_status != -1:
                os.system("cls")
                iface(manipulacije_menu, True, "Manipulacije")
                sub_status = input("Unesite odabir: ")
                try: 
                    int (sub_status)
                except ValueError: 
                    print("Unos mora biti broj!")
                    enter_to_continue()
                else:
                    sub_status = int (sub_status)     
                match sub_status:
                    case 0:
                        break
                    case 1:
                        os.system("cls")
                        rotate_meni = [90, 180, 270]
                        iface(rotate_meni, False,"Za koliko za koliko stupnjeva želite rotirati sliku?")
                        rotacija = int(input("Vaš odabir: "))
                        match rotacija:
                            case 1:
                                foto_edit = foto.transpose(Image.ROTATE_90).show()                                
                            case 2:
                                foto_edit = foto.transpose(Image.ROTATE_180).show()
                            case 3:
                                foto_edit = foto.transpose(Image.ROTATE_270).show()
                        break
                    case 2:
                        os.system("cls")
                        zrcaljenje_meni = ["Gore prema dolje", "Lijevo prema desno"]
                        iface(zrcaljenje_meni, False,"U kojem smjeru želite zrcaliti sliku? ")
                        rotacija = int(input("Vaš odabir: "))
                        match rotacija:
                            case 1:
                                foto_edit = foto.transpose(Image.FLIP_TOP_BOTTOM).show()                                                                
                            case 2:
                                foto_edit = foto.transpose(Image.FLIP_LEFT_RIGHT).show()
                            
                        break
        case 2:
            sub_status = 0
            while sub_status != -1:
                os.system("cls")
                iface(filteri_menu, True, "Filteri")
                sub_status = input("Unesite odabir: ")
                try: 
                    int (sub_status)
                except ValueError: 
                    print("Unos mora biti broj!")
                    enter_to_continue()
                else:
                    sub_status = int (sub_status)
                match sub_status:
                    case 0:
                        break
                    case 1:
                        img01 = foto.filter(ImageFilter.CONTOUR).show()
                    case 2:
                        img02 = foto.filter(ImageFilter.EDGE_ENHANCE).show()    
                    case 3:
                        img04 = foto.filter(ImageFilter.EMBOSS).show()
                    case 4:
                        img05 = foto.filter(ImageFilter.FIND_EDGES).show()
                    case 5:
                        img06 = foto.filter(ImageFilter.SHARPEN).show() 
                    case 6:
                        img07 = foto.filter(ImageFilter.SMOOTH).show()                                            
                    case 7:
                        img09 = foto.filter(ImageFilter.BoxBlur(radius=3)).show()   
                    case 8:
                        img10 = foto.filter(ImageFilter.GaussianBlur(radius=8)).show()
                    case 9:
                        img11 = foto.filter(ImageFilter.UnsharpMask(radius=7, percent=250, threshold=3)).show()                    
                    case 10:
                        img13 = foto.filter(ImageFilter.MedianFilter(size=7)).show()
                    case 11:
                        img12 = foto.filter(ImageFilter.MaxFilter(size=7)).show()
                    case 12:
                        img14 = foto.filter(ImageFilter.MinFilter(size=7)).show()
                break

