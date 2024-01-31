import random
import sys
import os
#ADD CODE FOR DEALER UNDER OR ABOVE 17 BEFORE LAST HAND CHECK
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "A"]

def blackjack():
    print("You are playing blackjack")
    my_first_hand = first_hand()

    players_cards = my_first_hand["players_cards"]
    dealers_cards = my_first_hand["dealers_cards"]
    player_score = my_first_hand["players_score"]
    dealer_score = my_first_hand["dealers_score"]

    first_next_card = input("Do you want another card? (Y/N)")
    
    if first_next_card.lower() == "n":
        hand_check(player_score, dealer_score, dealers_cards, players_cards)
        play_new_game = input("Do you want to play another game? (Y/N)")
        new_game(play_new_game)

    elif first_next_card.lower() == "y":
        score_after_new_card = next_hand(player_score, players_cards)
        player_score = score_after_new_card
        
        print("Score after another card", player_score)
    
    #Comparing final result to declare a winner
    hand_check(player_score, dealer_score, dealers_cards, players_cards)
    play_new_game = input("Do you want to play another game? (Y/N)")
    new_game(play_new_game)

def first_hand():
    print("FIRST HAND..DEALING CARDS..")
    cards_dealt = 2
    players_cards = []
    dealers_cards = []
    players_sum = 0
    dealers_sum = 0

    for _ in range(cards_dealt):
        players_card = random.choice(cards)
        players_cards.append(players_card)
       
        if players_card == "A" and players_sum + 11 > 21:
            players_sum += 1
        elif players_card == "A" and players_sum + 11 <= 21:
            players_sum += 11
        else:
            players_sum += players_card

        dealers_card = random.choice(cards)
        dealers_cards.append(dealers_card)
        
        if dealers_card == "A" and dealers_sum + 11 > 21:
            dealers_sum += 1
        elif dealers_card == "A" and dealers_sum + 11 <= 21:
            dealers_sum += 11
        else:
            dealers_sum += dealers_card
        
    print(f"PLAYERS HAND: {players_cards}")
    print(f"DEALERS HAND: [{dealers_cards[0]} *]")
    
    if players_sum == 21:
        print("BLACKJACK!!YOU WIN")
        play_new_game = input("Do you want to play another game? (Y/N)")
        new_game(play_new_game)

    first_hand = {"players_score": players_sum, "players_cards": players_cards, "dealers_score": dealers_sum, "dealers_cards": dealers_cards}
    
    return first_hand

def next_hand(current_score, current_cards):
    score_now = current_score
    
    next_card = random.choice(cards)
    
    if next_card == "A" and score_now + 11 > 21:
            score_now += 1
    elif next_card == "A" and score_now + 11 <= 21:
        score_now += 11
   
    else:
        score_now += next_card
    
    current_cards.append(next_card)
    print("Players cards after HIT ME", current_cards)
    print("SCORE: ",score_now)
    if score_now > 21:
        print("Score is over 21. DEALER WINS!!")
        play_new_game = input("Do you want to play another game? (Y/N)")
        new_game(play_new_game)

    another_card = input("Do you want another card?(Y/N)")
    
    if another_card.lower() == "y":
        next_hand(score_now, current_cards)
    
    return score_now

def hand_check(player_sum, dealer_sum, dealers_cards, players_cards):
   
        if player_sum == 21:
            print(f"BLACKJACK!! You WIN!\n Dealers cards {dealers_cards}, your cards {players_cards}")
        elif player_sum > 21:
            print(f"DEALER WINS!!\n Dealers cards {dealers_cards}, your cards {players_cards}")
        elif player_sum < 21 and player_sum > dealer_sum:
            print(f"YOU WIN!!\n Dealers cards {dealers_cards}, your cards {players_cards}")
        elif player_sum < 21 and player_sum < dealer_sum:
            print(f"DEALER WINS!!\n Dealers cards {dealers_cards}, your cards {players_cards}")
        elif player_sum == dealer_sum:
            print(f"IT IS A DRAW!\n Dealers cards {dealers_cards}, your cards {players_cards}")
    

def new_game(play_new):
    if play_new.lower() == "y":
        clear_screen()
        blackjack()
    else:
        print("You chose not to play another game of blackjack")
        sys.exit()

def clear_screen():
    os.system("cls")

mygame = blackjack()

