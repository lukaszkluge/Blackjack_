import pytest
import random

CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


CARDS = list(range(1, 12))               # Przykładowa talia kart: wartości od 1 do 11

def pc_card():
    while True:
        card = random.sample(CARDS, 2)
        computer = [card[0], card[1]]
        if sum(computer) >= 17:          # Sprawdzamy, czy początkowa suma spełnia warunek
            break
    while sum(computer) < 17:            # Jeśli nadal chcemy wymusić minimalną sumę 17
        next_card = random.choice(CARDS)
        if sum(computer) + next_card > 21:
            break
        computer.append(next_card)
    return computer


def test_pc_card_returns_list():
    result = pc_card()
    assert isinstance(result, list)


def test_pc_card_returns_list_of_integers():
    result = pc_card()
    assert all(isinstance(card, int) for card in result)


def test_pc_card_returns_list_of_length_at_least_2():
    result = pc_card()
    assert len(result) >= 2


def test_pc_card_returns_list_with_sum_less_than_or_equal_to_21():
    result = pc_card()
    assert sum(result) <= 21


def test_pc_card_returns_list_with_sum_greater_than_or_equal_to_17():
    result = pc_card()
    assert sum(result) >= 17
