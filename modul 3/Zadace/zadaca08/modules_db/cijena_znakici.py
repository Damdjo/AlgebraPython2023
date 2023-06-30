import os, json
#os.chdir("m3/Zadace/zadaca08")

def sterilize(kategorija:str, path:str=""):
    data = {}
    try:
        with open(f"{path}{kategorija}.json", "r" , encoding="utf-8") as fr:
            data = fr.read()
            
            
            data = data.replace("cijena Kn","cijena_Kn")
            data = data.replace("cijena €","cijena_€")
            data = data.replace("sifra artikla","sifra_artikla")
                
            
            data = json.loads(data)
            fr.close()
    except Exception as e:
        print(f"Error: {e}")

    

    edited = data   
    if edited != {}:
        try:
            with open(f"{path}{kategorija}.json", "w" , encoding="utf-8") as fw:
                edited = json.dumps(edited, indent=4, ensure_ascii=False)
                fw.write(edited)
                fw.close()

        except Exception as e:
            print(f"Error: {e}")

def main():
    sterilize("laptopi_data","site_data/podatci/")


if __name__ == "__main__":
    main()