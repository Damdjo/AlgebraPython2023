celsius = float(input("Unesite temperaturu u °C: "))

#formula za pretvorbu u Fahrenheit | °F = (°C x 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

#formula za pretvorbu u Kelvin | °K = °C + 273.15
kelvin = (celsius + 273.15)


print(f"Temperatura od {celsius}°C iznosi {int(fahrenheit)}F i {int(kelvin)}K")