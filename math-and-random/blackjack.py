import random

def getCards():

    given_cards = []

    for _ in range(2):
        card = random.choice(deck)
        deck.remove(card)
        given_cards.append(card)

    return given_cards

def formatDeck(deck, score):
    formatedDeck = f"{deck[0]} y {deck[1]}, suman {score} puntos"
    

    return formatedDeck

def calcScore(hand):
    card_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    total_score = 0
    for i in hand:
        score = card_values.get(i)
        if i == "A" and total_score + score > 21:
            total_score+=1

        else:
            total_score+=score

    return total_score

def askForACard():
    card = random.choice(deck)
    deck.remove(card)
    return card

def decideWin(player_score, dealer_score):

    if player_score > dealer_score:
        print("Has ganado")

    else:
        print("Has perdido")


stay = False
ended = False


deck = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"] * 4


player_cards = getCards()
dealer_cards = getCards()



user_option = ""

while not stay and not ended:
    player_score = calcScore(player_cards)
    dealer_score = calcScore(dealer_cards)
    
    if player_score > 21:
        ended = True
        print(f"Has perdido... ({player_score})")

    elif dealer_score > 21:
        ended = True
        print("Has ganado")

    if not ended:
        print(f"Tienes {formatDeck(player_cards,player_score)}")
        print(f"El dealer tiene {formatDeck(dealer_cards,dealer_score)}")
        print()
        user_option = input("¿Que deseas hacer, plantarte (s) o pedir carta (a)? ").lower()

        match user_option:

            case 's':
                stay = True

                if dealer_score < 17:
                    while dealer_score < 17:
                        dealer_cards.append(askForACard())
                        calcScore(dealer_cards)

                decideWin(player_score, dealer_score)
                

            case 'a':
                player_cards.append(askForACard())
            


