from random import choice
from day11 import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def check_for_aces(sel_cards):
    checked_cards = []
    if sum(sel_cards) > 21:
        for card in sel_cards:
            if card == 11:
                checked_cards.append(1)
            else:
                checked_cards.append(card)
        return checked_cards
    else:
        return sel_cards

def init_game():
    user_cards = []
    computer_cards = []

    start_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game == "y":
        print("\n"*20)
        # deal 2 cards each
        print(art.logo)
        user_cards.append(deal_card())
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        computer_cards.append(deal_card())

        user_cards = check_for_aces(user_cards)
        computer_cards = check_for_aces(computer_cards)

        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0:-1] + ["*"]}")

        # if user has less than 21 ask to hit another card
        if  sum(user_cards) < 21:
            new_card = input("\nType 'y' to get another card, type 'n' to pass: ")
            while new_card == "y":
                user_cards.append(deal_card())
                user_cards = check_for_aces(user_cards)
                if (sum(computer_cards) < 17) and (sum(user_cards) <= 21):
                    computer_cards.append(deal_card())
                    computer_cards = check_for_aces(computer_cards)
                if sum(user_cards) < 21:
                    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                    print(f"Computer's cards: {computer_cards[0:-1] + ["*"]}")
                    new_card = input("\nType 'y' to get another card, type 'n' to pass: ")
                else:
                    new_card = "n"

        # if computer is losing and has less than 17 hit another card
        while (sum(computer_cards) < 17) or ((sum(user_cards) > sum(computer_cards)) and (sum(user_cards) < 21)):
            computer_cards.append(deal_card())
            computer_cards = check_for_aces(computer_cards)

        # print final score
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}\n")

        #result
        if sum(user_cards) > 21:
            print("You went over. You lose.")
        elif sum(user_cards) == 21:
            print("Blackjack! You won!")
        elif sum(computer_cards) == 21:
            print("Lose, opponent has Blackjack!")
        elif sum(user_cards) > sum(computer_cards):
            print("You win!")
        elif sum(computer_cards) > 21:
            print("Opponent went over. You win!")
        elif sum(computer_cards) == sum(user_cards):
            print("You lose. Same score.")
        else:
            print("You lose.")
        init_game()

init_game()