import random
from art import logo

print("Welcome to BlackJack game!")
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
computer = []
user = []


def pc_card():
    card = random.sample(CARDS, 2)
    computer.append(card[0])
    computer.append(card[1])
    while sum(computer) < 17:
        next_card = random.choice(CARDS)
        computer.append(next_card)
        return computer
    return computer


def user_card():
    card = random.sample(CARDS, 2)
    user.append(card[0])
    user.append(card[1])
    return user


def user_next_card():
    should_continue = True
    while should_continue:
        if input("Do you want 1 more card? y - Yes, n - No: ").lower() == "y":
            next_card = random.choice(CARDS)
            user.append(next_card)
            print(f"{user}")
        else:
            should_continue = False
    return user


def sum_card():
    sum_computer = sum(computer)
    sum_user = sum(user)
    if sum_user < sum_computer <= 21:
        print(f"Computer win! Computer Cards: {computer}, Your cards: {user}")
    elif sum_computer < sum_user <= 21:
        print(f"You win! Your cards: {user}, Computer cards: {computer}")
    elif sum_computer > 21 >= sum_user:
        print(f"You win! Your cards: {user}, Computer cards: {computer}")
    elif sum_user > 21 >= sum_computer:
        print(f"Computer win! Computer Cards: {computer}, Your cards: {user}")
    elif sum_user == sum_computer:
        print("Push")


def reset_data():
    global user
    global computer
    user = []
    computer = []


def game():
    print(logo)
    if input("Deal the cards? y - yes, n - no: ").lower() == "y":
        pc_card()
        user_card()
        print(f"Computer cards: {computer[0]}\nUser cards: {user}")
        user_next_card()
        sum_card()
        if input("Play again? y - yes, n - no: ") == "y":
            reset_data()
            game()
        else:
            print("Good Bye!")
    else:
        print("Good Bye!")


game()
