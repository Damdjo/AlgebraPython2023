population = {
    "12345678901":"Petar Perić",
    "10987654321":"Marko Marić",
    "15976312345":"Ivan Ivić",
    "95135798765":"Josip Josipović"
}

element = population["12345678901"]
print(element)

print(population["95135798765"])

population["95135798765"] = "Mate Matić"
print(population["95135798765"])

print(population)

for key in population.keys():
    print(key, end = "; ")
print("\n")

for value in population.values():
    print(value, end = "; ")
print("\n")

for key, value in population.items():
    print(key, value, end = "; ")
print("\n")

