"""

A) Praćenje vježbi putem smartwatcha/fitness trackera
    1. Prikupljanje podataka
        -nakon što korisnik pritisne tipku za početak vježbe putem senzora na satu (akcelerometar, žiroskop) bilježi se pokret(broj ponavljanja)
        -pritiskom na istu tipku prestaje snimanje pokreta


    2. Čišćenje i prilagodba podataka
        #Čišćenje
        -u početku vježe potreban je kraći "grace" period u kojem se zanemaruju podatci o pokretu kako se ne bi registrirala kriva vježba
        -isto tako se određena odstupanja usred serije zanemaruju

        #Prilagodba
        -u samom početku korištenja sata/tek nakon što je kupljen koriste se preseti za vježbe no kako sat prikuplja podatke onda se isti personaliziraju prema korisniku

    
    3. Analiza, vizualizacija i interpretacija podataka        
        -nakon završetka treninga korisniku se izrađuje izvještaj treninga u kojemu ima ispisanu vrstu vježbe, broj serija, broj ponavljanja te kilaža sa kojom je vježba rađena


    4. Revizija podataka
        -korisnik izvještaj treninga može uređivati te ukoliko je neka od vježbi krivo prepoznata spremljeni podatci o pokretu se brišu

"""


"""
B) Praćenje korisnika web servisa (npr. Netflix) radi optimizacije pružanja usluge
    1. Prikupljanje podataka
        -svaki korisnik ima svoj username, povijest pregleda, regiju
        -nakon svakog pregleda zabilježava se username, naziv pregledanog sadržaja, regija


    2. Čišćenje i prilagodba podataka
        -podatci se sortiraju po regijama
        -za svaki pregledani sadržaj zabilježava se broj pregleda i regija korisnika

    
    3. Analiza, vizualizacija i interpretacija podataka
        -ovisno o broju pregleda sadržaja prema regiji alociraju se resursi:
            -velik broj pregleda znači više resursa te veći prioritet isporuke 
            -mali broj pregleda znači manje resursa te manji prioritet isporuke

        -isto tako se prati broj novih korisnika nakon premijere novog sadržaja te se shodno tome dodjeljuju novci za snimanje dodatnih nastavaka/sezona


    4. Revizija podataka
        -revizija se u pravilu odvija sama po sebi no može se dodatno ukoliko se primjete neka odstupanja

"""