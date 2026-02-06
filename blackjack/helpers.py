import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(hand):
    hand.append(random.choice(cards))
    return hand

def dealers_turn(computer_hand, user_hand):
    while sum(computer_hand) <= sum(user_hand) and sum(computer_hand) <= 21:
        deal_card(computer_hand)
    return computer_hand



def winner(hand1, hand2):
    sum1 = sum(hand1)
    sum2 = sum(hand2)

    if sum1 > 21:
        return hand2
    if sum2 > 21:
        return hand1
    if sum1 > sum2:
        return hand1
    else:
        return hand2


def sum_hand(hand):
    score = sum(hand)
    return score
