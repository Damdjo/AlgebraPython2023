#zad38 - Sustav članarina
#Lista ili Dictionary
#U listi index ili u dict ID (jedinstveni broj)
#Ostali podaci: 
#Ime, Prezime, Datum prvog učlanjenja (text), Članarina vrijedi do: (text), Razina (basic, premium)
#Funkcije/Opcije za: dodaj novog člana, izbriši člana, produži članarinu, izmjeni razinu
#pretraži člana po imenu/prezimenu i prikazi podatke
#napraviti default staticku listu od 10 clanova jer se ostalo brise svakim pokretanjem
 
clanovi=[['Mate','Matic','20210421','20230421','basic'],
         ['Ivo','Ivic','20200606','20230606','premium'],
         ['Jure','Juric','20180115','20221213','basic'],
         ['Stipe','Stipic','20190914','20230914','basic'],
         ['Lea','Lavic','20171019','20221019','premium'],
         ['Mare','Maric','20230509','20240509','basic'],
         ['Tonka','Tokic','20230404','20240404','premium'],
         ['Ruza','Cvitko','20220305','20230305','basic'],
         ['Kate','Konte','20211112','20231112','basic'],
         ['Marin','Mirni','20160421','20180421','premium']]
 
#clanovialt=[['Mate','Ivo','Jure'],['Matic','Ivic','Jurić']]
 
print(clanovi) #citava 2d lista
print(clanovi[0]) #podlista osobe na indeksu 0
print(clanovi[0][0]) #svojstvo osobe na indeksu 0 (MateMatic...), a koje je na indeksu 0 (ime)
 
print()
#print(clanovialt)
#print(clanovialt[0])
#print(clanovialt[0][0])
 
 
def provjeri():
    ime=input('Unesite ime: ')
    prezime=input('Unesite prezime: ')
    indeks=0
    pronadjeno=-1
    for clan in clanovi:
        print(clan)
        if ime in clan and prezime in clan:
            print(f'Pronasli smo trazenu osobu')
            pronadjeno=indeks
        indeks+=1
    return pronadjeno
 
def dodaj():
    #nekakav input podataka i provjera -> append u listu
    pass
 
def izbrisi():
    #provjera postoji li clan -> mogucnost brisanja (koju metodu???? google: python delete list element)
    print('Odaberite osobu koju zelite izbrisati:')
    indeks_brisanja=provjeri()
    print(indeks_brisanja)
    clanovi.pop(indeks_brisanja)
    pass
 
def produzi():
    #provjera postoji li clan -> trajanje danas+365 ili zadnji dan>danas -> zadnji dan+365
    print('Odaberite osobu kojoj zelite produziti clanarinu:')
    indeks_produzenja=provjeri()
    godina=clanovi[indeks_produzenja][3]
    intgodina=int(godina)
    intgodina+=10000
    strgodina=str(intgodina)
    clanovi[indeks_produzenja][3]=strgodina
 
    pass
 
def razina():
    #provjera postoji li clan -> izmjeni razinu (pristup elementu 'razina' u podlisti)
    #ispisati postojecu razinu i ponuditi suprotnu basic->premium ili obratno
    pass
 
def prikazi():
    #provjera postoji li clan -> ispis clana! 
    #ispis 
    pass
 
 
 
#neka fukcija za provjeru clanstva koju cemo reciklirat za sve ove prethodne funkcije
clan=['Mate','Matic','20210421','20230421','basic']
if clan in clanovi:
    print('Imamo Matu!') #imamo listu sa svim identicnim podacima
else:
    print('Nemamo Matu pregledom vanjske liste')
 
if 'Mate' in clanovi:
    print('Imamo Matu!') #nemamo matu
else:
    print('Nemamo Matu pregledom vanjske liste')
 
if 'Mate' in clanovi[0]:
    print('Imamo Matu!') #imamo ga! 
 
'''
print()
indeks_u_listi_clanova=0
pronadjeno=-1
for clan in clanovi:
    print(clan)
    if 'Maric' in clan:
        print(f'Pronasli smo prezime Maric!!!')
        pronadjeno=indeks_u_listi_clanova
    indeks_u_listi_clanova+=1
 
print(f'Maric je pronadjena na indeksu {pronadjeno}')
 
print(f'Podaci za pronadjenu osobu su:\n{clanovi[pronadjeno][0]} {clanovi[pronadjeno][1]} s danom\
 učlanjenja {clanovi[pronadjeno][2]} i trajanjem članarine do {clanovi[pronadjeno][3]} statusa\
 {clanovi[pronadjeno][4]}')
 
print()
 
print(provjeri())
'''
 
 
print(clanovi)
 
#izbrisi()
produzi()
 
print(clanovi)
 