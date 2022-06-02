import random
#Blackjack (formerly Black Jack and Vingt-Un) is a casino banking game.[1]: 342  The most widely played casino banking game in the world, it uses decks of 52 cards and descends from a global family of casino banking games known as Twenty-One

def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
   if sum(cards)==21 and len(cards)==2:
       return 0

   if 11 in cards and sum(cards)>21:
       cards.remove(11)
       cards.append(1)
   return sum(cards)

def compare(user_score,cmp_score):
    if user_score==cmp_score:
        return "DRAW"
    elif user_score==0:
        return "Win with a blackjack"
    elif cmp_score==0:
        return "Loose,Computer has blackjack"
    elif user_score>21:
        return "You went over and lost"
    elif cmp_score > 21:
        return "Computer went over and lost"
    elif user_score>cmp_score:
        return "You WON"
    else:
        return "You loose"

def play_game():
    user_card=[]
    comp_card=[]
    is_game=False
    for _ in range(2):
        user_card.append(deal_cards())
        comp_card.append(deal_cards())



    while not is_game:

        user_score=calculate_score(user_card)
        cmp_score=calculate_score(comp_card)
        print(f"    Your Cards :{user_card},current score : {user_score} ")
        print(f"    Computer's firstCard :{comp_card[0]}")

        if user_score==0 or cmp_score==0 or user_score>21:
             is_game=True
        else:
            user_input=input("Type 'y' to get a new card,type'n' to pass ")
            if user_input=='y':
                user_card.append(deal_cards())
            else:
                is_game=True
        while cmp_score!=0 and cmp_score<17:
            comp_card.append(deal_cards())
            cmp_score=calculate_score(comp_card)

        print(f"Your final hand :{user_card}, final score :{user_score} ")
        print(f" Computer final hand :{comp_card},final score :{cmp_score}")
        print(compare(user_score,cmp_score))

while input("Do you want to play game of blackjack? type 'y' or 'n': ")=="y":
   # clear()
    play_game()
