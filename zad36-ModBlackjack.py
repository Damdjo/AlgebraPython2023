# Modificirani blackjack

# Vrijednosti karata: 2-10, | J,Q,K-> 10 | A - 1 ili 11
# Daj kartu (random karta) ili Ostani (zadovoljni sa izvucenim)
# 
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

playerHand = []
playerSum = 0

dealerHand = []
dealerSum = 0

whooseTurn = "Player"

gameEnd = False

def dajKartu():
    roll = random.choice(deck)
    return roll 


def start():
    global playerHand
    global dealerHand
    for initial in range(2):
        playerHand.append(dajKartu())
        dealerHand.append(dajKartu())

def hit(playerOrDealer):
    global playerHand
    global dealerHand
    if playerOrDealer == "Player":    
        playerHand.append(dajKartu())
    elif playerOrDealer == "Dealer":
        dealerHand.append(dajKartu())

def playerTurn():
    global whooseTurn
    print("Vaše trenute karte su: ")
    for card in playerHand:
        print("\t",card, end = "")
    print("\nŽelite li dodatnu kartu (hit) ili ne (stand) ?\n")
    notStand = str(input(" Unesite DA za hit ili NE za stand: "))
    counter(playerHand)
    if playerSum < 22:
        if notStand == "DA" or notStand == "Da" or notStand == "da":
            notStand = True
            hit("Player")
        else:
            notStand = False
            whooseTurn = "Dealer"
            krajRunde = counter(playerHand)
            print(f"Zbroj vaših karti je {playerSum}")
    else:
        print("PREKORAČENJE")
    krajRunde = counter(playerHand)
        
    print("counter")
    #krajRunde = counter(playerHand)
    return notStand, krajRunde

def dealerTurn():
    global whooseTurn
    global dealerSum
    print("Trenutne karte dilera su: ")
    for card in dealerHand:
        print("\t",card, end = "")
    counterDealer(dealerHand)

    if dealerSum < 17 and dealerSum < playerSum: 
            hit("Dealer")
            print(f"\nDealer si je odličio dodijeliti novu kartu ({dealerHand[-1]})!")
    else:
        whooseTurn = "End"

    krajRunde = counterDealer(dealerHand)      

    
    return krajRunde

    


def turn(playerOrDealer):
    global whooseTurn
    global dealerSum
    global gameEnd
    kraj = False
    krajDealer = False
    print("*"*60)
    if whooseTurn == "Player" and kraj != True:
        notStand, kraj = playerTurn()      
        while notStand == True:
            notStand, kraj = playerTurn()
            if kraj == True:
                break
    #LOGIKA ZA DEALER POTEZE
    elif whooseTurn == "Dealer" and krajDealer != True:
        krajDealer = dealerTurn()

    else:
        gameEnd = True
        print("ENDENDENDENDENDENDENDENDEND")
        
        
    return kraj, krajDealer

     
        
    

def jedanIli10():
    print("Jedna od karti u vašoj ruci je \"A\"")
    koliko = int(input("Želite li da se \"A\" broji kao 1 ili kao 11: "))
    return koliko


def counter(hand):
    global playerSum
    global gameEnd
    playerSum = 0
    kraj = False
    for card in hand:
        
        if card == "J" or card == "Q" or card == "K":
            hand.remove(card)
            hand.append(10)
            playerSum += 10
        elif card == "A":
            hand.remove(card)
            card = int(jedanIli10()) 
            hand.append(card)
            playerSum += card
        
        else:
            playerSum += card
    if playerSum == 21:
        print("\nPobijedili ste")
        kraj = True
        gameEnd = True
    elif playerSum > 21:
        print(f"\nIzgubili ste, zbroj vaših karti je: {playerSum}")
        kraj = True
        gameEnd = True
    return kraj

def counterDealer(hand):
    global dealerSum
    global gameEnd
    dealerSum = 0
    kraj = False
    for card in hand:
        
        if card == "J" or card == "Q" or card == "K":
            hand.remove(card)
            hand.append(10)
            dealerSum += 10
        elif card == "A":
            hand.remove(card)
            hand.append(11)
            dealerSum += 11
        
        else:
            dealerSum += card
    if dealerSum == 21:
        print("\nDealer ima blackjack")
        kraj = True
        gameEnd = True
    elif dealerSum > 21:
        print(f"\nPobijedili ste, zbroj karti dilera je: {dealerSum} TEST")
        kraj = True
        gameEnd = True
    
    return kraj



start()
playerHandInit = playerHand
dealerHandInit = dealerHand
print(f"Vaše karte su: ")

for card in playerHandInit:
    print(card,"\t", end = "")
print()
print(f"Karte dealera su: ")
for card in dealerHandInit:
    print(card,"\t", end = "")
print()

whooseTurn = "Player"
gameEnd = False
while gameEnd != True:    
    krajPlayer, krajDealer = turn(whooseTurn)
    if krajPlayer == True and krajDealer == True:
        gameEnd = True
        break


print(playerHand,dealerHand)
print(playerSum,dealerSum)



