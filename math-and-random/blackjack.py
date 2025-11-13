import random

def getCards(deck):

    given_cards = []

    for _ in range(2):
        card = random.choice(deck)
        deck.remove(card)
        given_cards.append(card)

    return given_cards

def formatDeck(deck, score):
    # Unimos todas las cartas con comas y una 'y' antes de la última
    if len(deck) > 1:
        cartas = ', '.join(deck[:-1]) + f" y {deck[-1]}"
    else:
        cartas = deck[0]
    
    return f"{cartas}, suman {score} puntos"

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

def askForACard(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def decideWin(player_score, dealer_score):

    if player_score > dealer_score:
        print("Has ganado")

    else:
        print("Has perdido")

def blackjack():

    stay = False
    ended = False


    deck = ["K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"] * 4


    player_cards = getCards(deck)
    dealer_cards = getCards(deck)


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

        while user_option not in ['s', 'a']:
            user_option = input("Opción no válida. Escribe 's' para plantarte o 'a' para pedir carta: ").lower()

        match user_option:
            case 's':
                stay = True
                if dealer_score < 17:
                    while dealer_score < 17:
                        dealer_cards.append(askForACard(deck))
                        dealer_score = calcScore(dealer_cards)
                decideWin(player_score, dealer_score)
                
            case 'a':
                player_cards.append(askForACard(deck))

blackjack()