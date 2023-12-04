import pytest
from dice import Dice, Hand
def test_create_dice():
    dice = Dice(4, 2)

def test_create_dice_wrong_num_of_walls():
    with pytest.raises(ValueError):
       dice = Dice(3, 2) 

def test_create_dice_wrong_num_of_rolls():
    with pytest.raises(ValueError):
        dice = Dice(4, -1)

def test_roll(monkeypatch):
    def roll_one(f, t):
        return 1
    monkeypatch.setattr('dice.randint', roll_one)
    dice = Dice(4, 2)
    assert dice.roll() == 1
    
def test_hand_roll(monkeypatch):
    def roll_one(f, t):
        return 1
    monkeypatch.setattr('dice.randint', roll_one)
    dice1 = Dice(4, 2)
    dice2 = Dice(6, 2)
    dice3 = Dice(8,2)
    hand = Hand([dice1, dice2, dice3])
    assert hand.roll_dices() == [1, 1, 1]

def test_hand_roll(monkeypatch):
    def roll_one(f, t):
        return 1
    monkeypatch.setattr('dice.randint', roll_one)
    dice1 = Dice(4, 2)
    dice2 = Dice(6, 2)
    dice3 = Dice(8,2)
    hand = Hand([dice1, dice2, dice3])
    hand.roll_dices()
    assert hand.sum_roll() == 3

def test_re_roll(monkeypatch):
    def roll_one(f, t):
        return 1
    monkeypatch.setattr('dice.randint', roll_one)
    dice1 = Dice(4, 2)
    dice2 = Dice(6, 2)
    dice3 = Dice(8,2)
    hand = Hand([dice1, dice2, dice3])
    hand.roll_dices()
    hand.re_roll(1)
    assert dice1.rolls == 0



def test_compare_to_other(monkeypatch):
    def roll_one(f, t):
        return 1
    monkeypatch.setattr('dice.randint', roll_one)
    dice1 = Dice(4, 2)
    dice2 = Dice(6, 2)
    dice3 = Dice(8,2)
    hand = Hand([dice1, dice2, dice3])
    hand2 = Hand([dice1, dice2])
    hand.roll_dices()
    hand2.roll_dices()
    hand.compare_to_other(hand2)
    assert hand.did_win == True
    assert hand2.did_win == False

