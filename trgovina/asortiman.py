import proizvodi

# proizvod={'id':'abc123', 'opis':'Maslo Megle 250g', 'cijena':18.90, 'stanje':132}

asortiman = [    
                proizvodi.banane, 
                proizvodi.bronhi_original, 
                proizvodi.jogurt_bioaktiv, 
                proizvodi.kakao_kras,
                proizvodi.kitkat,
                proizvodi.majoneza_zvijezda,
                proizvodi.masloMeggle,
                proizvodi.milka_keks,
                proizvodi.rizle,
                proizvodi.sok_fis,
                proizvodi.tortilla_wrap
            ]


def provjeri_stanje(lista_proizvoda:list, id:str):

    #print(lista_proizvoda)
    #print(lista_proizvoda[0])
    #print(lista_proizvoda[0]["id"])

    for proizvod in lista_proizvoda:
        if proizvod["id"] == id:
            return proizvod["stanje"]

   
    return None
    #vratimo stanje proizvoda

def potrebno_nabaviti(lista_proizvoda:list, minimalno_stanja:int):
    lista_za_naruciti = []
    for proizvod in lista_proizvoda:
        if proizvod["stanje"]<minimalno_stanja:
            lista_za_naruciti.append(proizvod["id"])
    return lista_za_naruciti



def main():
    
    pass 






















if __name__ == "__main__":
    main()