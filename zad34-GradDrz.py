# Grad-država igra (u listu ili dictionary ubaciti parove gl.grad - država i random izvlačiti za igru)
# u listu ili dictionary ubaciti niz parova država-grad koje ćemo koristiti u igri
# random izvlačiti "računalno" odabrani grad ili zemlju, pa tražiti od korisnika da unese drugi dio
#brojati pokušaje u obliku X/Y ili "samo" točno / netočno

import random
status = -1
tries = 0
guesses = 0

dictCityState = {

"Austria": "Vienna",
"Belgium": "Brussels",
"Bulgaria": "Sofia",
"Croatia": "Zagreb",
"Cyprus": "Nicosia",
"Czech Republic": "Prague",
"Denmark": "Copenhagen",
"Estonia": "Tallinn",
"Finland": "Helsinki",
"France": "Paris",
"Germany": "Berlin",
"Greece": "Athens",
"Hungary": "Budapest",
"Ireland": "Dublin",
"Italy": "Rome",
"Latvia": "Riga",
"Lithuania": "Vilnius",
"Luxembourg": "Luxembourg",
"Malta": "Valleta",
"Netherlands": "Amsterdam",
"Poland": "Warsaw",
"Portugal": "Lisbon",
"Romania": "Bucharest",
"Slovakia": "Bratislava",
"Slovenia": "Ljubljana",
"Spain": "Madrid",
"Sweden": "Stockholm"
}

states = []
for key in dictCityState.keys():
    states.append(key)

cities = []
for value in dictCityState.values():
    cities.append(value)

def randChoice():
    global dictCityState
    global states
    global cities
    cityOrState = random.randint(0,1)
    if cityOrState == 0:
        genChoice = random.choice(states)
    else:
        genChoice = random.choice(cities)
    
    return genChoice, cityOrState

def isCorrect(generated, cityState):
    global status
    global states
    global cities
    global tries
    global guesses
    
    if cityState == 0:
        response = input("Your answer is: ")        
        correct = states.index(generated)
        answer = ""
        if response in cities:
            answer = cities.index(response)
        elif response == "0":
            status = 0
        else:
            print("That state is not in EU")
            tries += 1
                
        if answer == correct:
            print("Correct")
            guesses += 1
            tries += 1
        else:
            print("False")
    if cityState == 1:
        response = input("Your answer is: ")        
        correct = cities.index(generated)
        answer = ""
        if response in states:
            answer = states.index(response)
        elif response == "0":
            status = 0
            
        else:
            print("That city is not in EU")
            tries += 1
        
        if answer == correct:
            print("Correct")
            guesses += 1
            tries += 1
        else:
            print("False")
    return status



def genQuestion(cityState,choice):

    if choice == 0:
        print(f"What is the capital of the state of {cityState}: ")
        question = cityState
        

    elif choice == 1:
        print(f"Which state is {cityState} the capital of: ")
        question = cityState
        

    else:
        print("ERROR!")   
    
    return question, choice








while status != 0:
    choice, cityOrState = randChoice()
    question, ansKey = genQuestion(choice,cityOrState)
    isCorrect(question, ansKey)

print(f"Od ukupno {tries} pokušaja, pogodili ste {guesses} puta.")