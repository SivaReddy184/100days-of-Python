import random


def get_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if sum(card) > 21 and 11 in card:
        card.remove(11)
        card.append(1)
    return sum(card)


def compare(user_score, computer_score):
    # Bug fix. If you and the computer are both over, you lose.
    # new comment
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def game():
    game_over = False
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(get_cards())
        computer_cards.append(get_cards())
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards are{user_cards} and your current score is {user_score}")
        print(f"computer's first card : {computer_cards[0]} ")
        print("        ------------------------------------              ")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_card = input("do you want to draw another card? type 'y' to draw or type 'n' to pass ")
            if draw_card == "y":
                user_cards.append(get_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(get_cards())
        computer_score = calculate_score(computer_cards)
    print("                   ----------------                                       ")
    print(f"your cards are{user_cards} and your total score is {user_score}")
    print(f"computer cards are {computer_cards} and computer score is {computer_score} ")
    print(compare(user_score, computer_score))
    print("-------------------------------------------------------------------------------")


while input("Do you want to play black jack? type 'y' or 'n' ") == "y":
    game()
