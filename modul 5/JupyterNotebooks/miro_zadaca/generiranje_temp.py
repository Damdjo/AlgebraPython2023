import random
from datetime import datetime, timedelta

# Funkcija za generiranje nasumičnih promjena temperature tijekom vremena
def generate_temperature_changes(current_temperature, month, time_of_day):
    # Definirajte maksimalne i minimalne temperature ovisno o mjesecu i dobu dana
    temperature_ranges = {
        1: {"jutro": (-25, -15), "dan": (-15, -5), "noc": (-20, -10)},
        2: {"jutro": (-20, -10), "dan": (-10, 0), "noc": (-15, -5)},
        3: {"jutro": (-15, -5), "dan": (-5, 5), "noc": (-10, 0)},
        4: {"jutro": (-10, 0), "dan": (0, 10), "noc": (-5, 5)},
        5: {"jutro": (-5, 5), "dan": (10, 20), "noc": (5, 15)},
        6: {"jutro": (15, 20), "dan": (25, 35), "noc": (15, 20)},
        7: {"jutro": (20, 25), "dan": (30, 39), "noc": (20, 25)},
        8: {"jutro": (20, 25), "dan": (30, 39), "noc": (20, 25)},
        9: {"jutro": (10, 15), "dan": (20, 30), "noc": (15, 20)},
        10: {"jutro": (5, 10), "dan": (15, 25), "noc": (10, 15)},
        11: {"jutro": (-5, 0), "dan": (5, 15), "noc": (0, 10)},
        12: {"jutro": (-20, -10), "dan": (-10, 0), "noc": (-15, -5)},
    }


    min_temperature, max_temperature = temperature_ranges[month][time_of_day]

    # Nasumična promjena temperature
    temperature_change = random.uniform(-1, 1)  # Manje promjene
    new_temperature = current_temperature + temperature_change

    # Osiguraj da temperatura ostane unutar granica za odabrani mjesec i doba dana
    new_temperature = max(min_temperature, min(max_temperature, new_temperature))
    
    return new_temperature

# Unos početnog datuma i vremena od korisnika
start_date = input("Unesite početni datum (DD.MM.YYYY): ")
start_time = input("Unesite početno vrijeme (HH:MM): ")

try:
    start_datetime = datetime.strptime(start_date + ' ' + start_time, '%d.%m.%Y %H:%M')
except ValueError:
    print("Pogrešan format datuma ili vremena. Molimo unesite u formatu 'DD.MM.YYYY' i 'HH:MM'.")
    exit()

# Provjera minimalne razlike od dvije godine
if (datetime.now() - start_datetime).days < 730:
    print("Početni datum i vrijeme moraju biti najmanje dvije godine prije današnjeg datuma.")
    exit()

# Rječnik za pohranu podataka
data = {}
current_temperature = 20  # Početna temperatura

# Generiranje podataka za dvije godine
current_datetime = start_datetime
while current_datetime < datetime.now():
    month = current_datetime.month
    time_of_day = "jutro" if current_datetime.hour < 12 else "dan" if current_datetime.hour < 18 else "noc"

    temperature = generate_temperature_changes(current_temperature, month, time_of_day)
    humidity = round(random.uniform(15, 95), 2)    # Vlažnost od 15% do 95%
    pressure = round(random.uniform(990, 1035), 2) # Tlak zraka od 990 hPa do 1035 hPa
    
    data.setdefault(current_datetime.strftime('%d.%m.%Y'), []).append((current_datetime.strftime('%H:%M'), round(temperature, 2), humidity, pressure)) #type: ignore
    
    current_datetime += timedelta(minutes=15)
    current_temperature = temperature  # Postavite trenutnu temperaturu za sljedeći korak

# Ispis podataka
for date, values in data.items():
    month = datetime.strptime(date, '%d.%m.%Y').month
    time_of_day = values[0][0].split(':')[0]  # Uzmite prvo vrijeme iz svakog dana za određivanje doba

    print(f'Datum: {date}')
    for time, temp, hum, pres in values:
        print(f'  Vrijeme: {time}, Temperatura: {temp:.0f}°C, Vlažnost: {hum}%, Tlak: {pres} hPa')

