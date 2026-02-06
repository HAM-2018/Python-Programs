import art
from helpers import deal_card, winner, sum_hand, dealers_turn
import random


start_game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


while start_game == "y":
    print(art.logo)

    user_hand = []
    deal_card(user_hand)
    deal_card(user_hand)

    computer_hand = []
    deal_card(computer_hand)
    deal_card(computer_hand)

    score = sum_hand(user_hand)

    print(f"Your cards: {user_hand}, current score: {score}")
    print(f"Computer's first card: {computer_hand[0]}")

    hit = ""
    while hit != "n":
        hit = input("Type 'y' to hit, 'n' to pass: ").lower()


        if hit == "y":
            deal_card(user_hand)
            score = sum_hand(user_hand)
            print(f"Your cards: {user_hand}, current score: {score}")
            print(f"Computer's first card: {computer_hand[0]}")
            if score > 21:
                print("You busted. Dealer wins")
                break
        else:
            dealers_turn(computer_hand, user_hand)
            best_hand = winner(user_hand, computer_hand)
            if best_hand == user_hand:
                print(f"You win!! Your hand: {user_hand}  Dealer's hand: {computer_hand}")
            else:
                print(f"You Lose!! Your hand: {user_hand}  Dealer's hand: {computer_hand}")


    start_game = input("Play again? 'y' or 'n': ").lower()
