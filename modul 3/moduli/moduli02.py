import time, os , datetime as dt
from dateutil.relativedelta import relativedelta, TU, FR
from dateutil import tz
import locale

sadasnji_trenutak = dt.datetime.now()
novi_datum_objekt = dt.datetime.strptime("24. July 1975. 4:45:00","%d. %B %Y. %H:%M:%S")

razlika = sadasnji_trenutak - novi_datum_objekt

print(razlika)

#napisi program u koji ces u varijablu upisati svoj rodjendan
#ispisi koliko godina imas

danas = dt.datetime.now()
rodendan = dt.datetime.strptime("25. December 1997. 9:18:00","%d. %B %Y. %H:%M:%S")

starost = danas-rodendan
starost = int(starost.days/365)

print(f"Damjan ima {starost} godina.")

za_6_dana = sadasnji_trenutak+dt.timedelta(days=6)
print(za_6_dana)
prije_153_dana = sadasnji_trenutak+dt.timedelta(days=-153)
print(prije_153_dana)

rd = relativedelta(day=31, weekday=FR(-1))
print(f"Zadnji petak u mjesecu je {sadasnji_trenutak+rd}")

datum = dt.date(2023,4,3)
print(datum)
print(datum+rd)

tz_zg = tz.gettz("Europe/Zagreb")
termin_zg = dt.datetime(2023,6,8, tzinfo=tz_zg)
tz_ny = tz.gettz("America/New_York")
termin_ny = termin_zg.astimezone(tz_ny)

tz_hk = tz.gettz("Asia/Hong_Kong")
termin_hk = termin_zg.astimezone(tz_hk)

print(f"Termin u ZG počinje u {termin_zg.strftime('%d.%m.%Y %H:%M')}")
print(f"Termin u NY počinje u {termin_ny.strftime('%d.%m.%Y %H:%M')}")
print(f"Termin u HK počinje u {termin_hk.strftime('%d.%m.%Y %H:%M')}")