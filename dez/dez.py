class Magazine:
    def __init__(self, glicerine, aloes, alcohol, conservant):
        self.glicerine = glicerine * 1000
        self.aloes = aloes * 1000
        self.alcohol = alcohol * 1000
        self.conservant = conservant * 1000
        self.resources_list = [self.glicerine/1000, self.aloes/1000, self.alcohol/1000, self.conservant/1000]
    def check_order(self, gel=0, hand_liquid=0, floor_liquid=0):
        glicerine_cost =  gel*100 + hand_liquid*30 + floor_liquid*5
        aloes_cost = gel*350
        alcohol_cost = gel*600 + 720*hand_liquid + floor_liquid*800
        conservant_cost = (gel+hand_liquid+floor_liquid)*50
        if self.glicerine - glicerine_cost < 0:
            raise NotEnoughResourcesError
        if self.aloes - aloes_cost < 0:
            raise NotEnoughResourcesError
        if self.alcohol - alcohol_cost < 0:
            raise NotEnoughResourcesError
        if self.conservant - conservant_cost < 0:
            raise NotEnoughResourcesError
        return f'{glicerine_cost}ml of glicerine, {aloes_cost}ml of aloes, {alcohol_cost}ml of alcohol and {conservant_cost}ml of conservant is needed'
    

    def raport(self):
        print(f'| Zasób {("|"):>5} Ilość w magazynie [l] |')
        print(f'|{("-")*10} {("|"):>1} {("-")*21}:|')
        print(f'| gliceryna {("|"):>1}{int((self.glicerine/1000)):>23}|')
        print(f'| aloes {("|"):>5}{int((self.aloes/1000)):>23}|')
        print(f'| alcohol {("|"):>3}{int((self.alcohol/1000)):>23}|')
        print(f'| conservant{("|")}{int((self.conservant/1000)):>23}|')


class NotEnoughResourcesError(Exception):
    def __init__(self):
        super().__init__('There arent enough resources in the magazine')

magazine = Magazine(10, 10, 10, 10)
magazine.raport()