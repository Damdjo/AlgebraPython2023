from helpers import meni, validate_password


zadnji_id=0
#roles: admin, user
#status: active, disabled
korisnici=[
    {'id':0,'username':'admin','password':'admin','role':'admin','status':'active'}
]


menu_items=['Uredi profil','Izmjeni lozinku','Dodaj korisnika','Uredi korisnika']


#meni(menu_items,True) #prikaz menija za admina

#meni(menu_items[:2],True) # prikaz menija za korisnika

def unos_passworda():
    while True:
        password=input('Unesite password koji ćete koristiti (min. 8 znakova): ')
        if validate_password(password,8):
            break


"""
#ista stvar samo kraće:
print()
while True:
    if validate_password(input('Unesite password koji ćete koristiti (min. 8 znakova): '),8):
        break
"""
#print(validate_password('sdfjlslfjlsdlfjlk',20))

def ispisi_korisnika(korisnik:dict)->None:
    print(korisnik)
    print(f"ID: {korisnik['id']}, Username: {korisnik['username']}")
    #print(f"Ime: {korisnik['ime']}, Prezime: {korisnik['prezine']}")
    print(f"Uloga: {korisnik['role']}, Status: {korisnik['status']}")
   

def tip_korisnika(korisnik:dict)->str:
    return korisnik['role']

def postoji_korisnik(korisnici:list, korisnik:str)->tuple:
    for user in korisnici:
        if user['username']==korisnik:
            return (user['username'],user['password'],user['role'])
    return ()

def dohvati_korisnika(korisnici:list, korisnicki_username:str)->dict:
    for korisnik in korisnici:
        if korisnik['username']==korisnicki_username:
            return korisnik
    return {}


#def pass_korisnika(korisnici:list, )

#ispisi_korisnika(korisnici[0])
"""
print(tip_korisnika(korisnici[0]))

print('Unesite korisnicke podatke:')
user=input('Korisnicko ime: ')
lozinka=input('Lozinka: ')
if postoji_korisnik(korisnici, user):
    if postoji_korisnik(korisnici, user)[1]==lozinka:
        print('Lozinka je ispravna!admin')
        if postoji_korisnik(korisnici, user)[2]=='admin':
            meni(menu_items,True) #prikaz menija za admina
    else:
        print('Korisnički podaci su neispravni!')
"""

print(bool(dohvati_korisnika(korisnici,'admin')))





