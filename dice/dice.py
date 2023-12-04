from random import randint


class Dice:
    def __init__(self, walls, rolls):
        if walls/2  == int(walls/2) and walls > 2:
            self.walls = walls
        else:
            raise ValueError
        if rolls < 0:
            raise ValueError
        self.rolls = rolls

    def roll(self):
        self.rolls -= 1
        return randint(0, self.walls+1)

class Hand:
    def __init__(self, dices):
        self.dices = dices
        self.rolls = []
        self.did_win = False
        self.max_points = 0
        for dice in dices:
            self.max_points += dice.walls
    def roll_dices(self):
        self.rolls = []
        for dice in self.dices:
            if dice.rolls > 0:
                self.rolls.append(dice.roll())
        return self.rolls
    
    def re_roll(self, i):
        self.dices[i-1].roll()

    
    def sum_roll(self):
        return sum(self.rolls)

    def compare_to_other(self, other):
        if self.sum_roll() > other.sum_roll():
            self.did_win = True
        elif self.sum_roll() < other.sum_roll():
            other.did_win = False

    def report(self):
        for i, dice in enumerate(self.dices):
            print(f' * D{dice.walls}: {self.rolls[i]}')
        print(f'Total roll value: {self.sum_roll()}/{self.max_points}')

dice1 = Dice(4, 2)
dice2 = Dice(6, 2)
dice3 = Dice(8,2)
hand = Hand([dice1, dice2, dice3])
hand.roll_dices()
hand.report()

