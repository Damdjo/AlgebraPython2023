import datetime as dt
import locale 

danasnji_dan = dt.date.today()
print(f"Današnji dan je {danasnji_dan}")

sadasnji_trenutak = dt.datetime.now()
print(f"Sadasnji trenutak je {sadasnji_trenutak}")

dan_u_tjednu = dt.date.weekday(danasnji_dan)
print(f"Danas je {dan_u_tjednu+1}. dan u tjednu")

print()
print(locale.getlocale())
print(f"Puni naziv današnjeg dana u tjednu je {danasnji_dan.strftime('%A')}")
print(f"Skraceni naziv današnjeg dana u tjednu je {danasnji_dan.strftime('%a')}")



locale.setlocale(locale.LC_TIME, "hr_HR")
print(locale.getlocale())
print(f"Puni naziv današnjeg dana u tjednu je {danasnji_dan.strftime('%A')}")
print(f"Skraceni naziv današnjeg dana u tjednu je {danasnji_dan.strftime('%a')}")

locale.setlocale(locale.LC_TIME, "de_DE")
print(locale.getlocale(locale.LC_TIME))
print(f"Puni naziv današnjeg dana u tjednu je {danasnji_dan.strftime('%A')}")
print(f"Skraceni naziv današnjeg dana u tjednu je {danasnji_dan.strftime('%a')}")

locale.setlocale(locale.LC_ALL, "en_US")
print(locale.getlocale())
print(f"Puni naziv današnjeg dana u tjednu je {danasnji_dan.strftime('%A')}")
print(f"Skraceni naziv današnjeg dana u tjednu je {danasnji_dan.strftime('%a')}")

print()
print(f"Godina u obliku 4 znamenke: {danasnji_dan.strftime('%Y')}")
print(f"Godina u obliku 2 znamenke: {danasnji_dan.strftime('%y')}")

print()
print(f"Trenutni dan u godini je: {danasnji_dan.strftime('%j')}")
print(f"Trenutni tjedan u godini je: {danasnji_dan.strftime('%V')}")

# Danas je utorak, 06. lipanj 2023. godine
locale.setlocale(locale.LC_ALL, "hr_HR")
print(f"Danas je {danasnji_dan.strftime('%A')}, {danasnji_dan.strftime('%d. %B %Y.')} godine")

# Trenutno je 19h51m43s
print(f"Trenutno je {sadasnji_trenutak.strftime('%Hh%Mm%Ss')}")




