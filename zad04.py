snagaTrosila = int(input("Unesite snagu trošila u W: "))
cijenaPoKWh = float(input("Cijena kWh struje: "))
vrijemeKoristenjaUredaja = float(input("Vrijeme korištenja uređaja u satima: "))

potrosenaEnergijaKWh = snagaTrosila * vrijemeKoristenjaUredaja / 1000
ukupnaCijena = potrosenaEnergijaKWh * cijenaPoKWh

print(f"Ukupno ste potrošili {potrosenaEnergijaKWh} kWh energije.")
print(f"Cijena potrošene energije iznosi {ukupnaCijena} €")